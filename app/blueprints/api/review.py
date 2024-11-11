from flask import jsonify, request
from . import api_bp
from app.config import Config
from langchain.llms import OpenAI
import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)

llm = OpenAI(api_key=Config.OPENAI_API_KEY)

REVIEW_API_URL = Config.MAGICREVIEW_API_REVIEW
REVIEW_API_KEY = Config.MAGICREVIEW_API_KEY


def fetch_reviews():
    """Fetches reviews from the external API"""
    headers = {"X-API-Key": REVIEW_API_KEY}
    try:
        response = requests.get(REVIEW_API_URL, headers=headers)
        response.raise_for_status()
        logging.info(response.json())
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching reviews: {e}")
        return []


def filter_reviews_for_reply(reviews):
    """Filters reviews needing a reply"""
    to_reply = []
    for entity in reviews:
        for review in entity.get("reviews", []):
            if review["review_reply"] is None:
                to_reply.append((review, entity["info"], entity["entity_uuid"]))
    logging.info(f"{len(to_reply)} reviews filtered for replies.")
    return to_reply


def generate_reply(reviewer, comment, star_rating, business_description, replyer):
    """Generates a reply using OpenAI LLM"""
    prompt = f"""
    Reviewer: {reviewer}
    Business Description: {business_description}
    Review: {comment}
    Star Rating: {star_rating}
    Replyer: {replyer}
    Identify the review and star rating to determine the sentiment.
    Generate a polite and engaging reply according to the guidelines:
    - Thank the reviewer for their positive feedback.
    - Mention any specific details if provided.
    - Invite them to engage further with our products or services.
    - The reply should be between 200 to 400  characters.
    Generate a polite and apologetic response acknowledging any negative experience:
    - Offer to address specific complaints mentioned in the review.
    - Invite the reviewer to discuss their experience with us directly.
    - Commit to improving based on their feedback.
    - The reply should be between 200 to 400  characters.
    """

    try:
        reply = llm(prompt)
        logging.info("Reply generated successfully.")
        return reply
    except Exception as e:
        logging.error(f"Error generating reply: {e}")
        return "Thank you for your feedback!"


def create_reply_payload(reviews):
    """Formats the reviews with replies in the final API-ready structure"""
    reply_data = {}
    for review, info, entity_uuid in reviews:
        agent_reply = generate_reply(
            review["display_name"],
            review["comment"],
            review["star_rating"],
            info["description"],
            info["account_name"],
        )
        review_payload = {
            "review_id": review["review_id"],
            "profile_photo_url": review["profile_photo_url"],
            "display_name": review["display_name"],
            "star_rating": review["star_rating"],
            "comment": review["comment"],
            "create_time": review["create_time"],
            "update_time": review["update_time"],
            "review_reply": None,
            "review_reply_update_time": None,
            "agent_reply_draft": agent_reply,
            "agent_reply_time": datetime.utcnow().isoformat(),
        }

        if entity_uuid not in reply_data:
            reply_data[entity_uuid] = {"reviews": [], "entity_uuid": entity_uuid}

        reply_data[entity_uuid]["reviews"].append(review_payload)

    return list(reply_data.values())


@api_bp.route("/review-reply", methods=["GET"])
def review_reply():
    """Main endpoint for generating review replies"""
    reviews = fetch_reviews()
    if not reviews:
        return jsonify({"error": "Failed to fetch reviews"}), 500

    # Filter reviews needing a reply
    reviews_to_reply = filter_reviews_for_reply(reviews)

    # Create reply payload
    reply_payload = create_reply_payload(reviews_to_reply)
    logging.info("Reply payload generated.")

    return jsonify(reply_payload), 200
