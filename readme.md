# RUN PROJECT

```bash
pyenv global 3.12.2
docker-compose up -d --build
```

# PROJECT DESCRIPTION

Create an AI agent to reply to a list of reviews. The steps are:

1. Fetch the reviews from the structured api json response.
   API URL: https://magicreviewapi-dev0756.azurewebsites.net/external/data
   METHOD: GET
   HEADER: X-API-Key: wzWUs8MwPPFZugn2GEY0MljhpEJK0-vYM2YFKtrZ9-g
   The structure will be like:

```json
[
  {
    "info": {
      "account_name": "Info MagicPitch",
      "title": "Magicpitch LLC",
      "region_code": "AE",
      "administrative_area": "Dubai",
      "maps_uri": "https://maps.google.com/maps?cid=16828986524786053041",
      "new_review_uri": "https://search.google.com/local/writereview?placeid=ChIJzWsxMZlDXz4RsU-1mxSSjOk",
      "description": "Magicpitch is an Al powered, Data driven effective outreach Company that specializes in One-to-One Hyper-personalized outreach.\n\nFounded in April 2020, Magicpitch specialized in B2B sales development and provides data-driven, AI-powered hyper-personalized email outreach strategies to help businesses generate qualified leads."
    },
    "reviews": [
      {
        "review_id": "AbFvOqnaAuW3l8WRk5U5EpoSW3D5Gge_LAfihrjfZG8kmAcpF51qNzsvSHM6HWGXrJaa0kdHCzSEQw",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjW0zpyANp8lusdImCJR5-9gXViP3LMOC1HM-ke4_fdc0Bf52Zvs=s120-c-rp-mo-ba3-br100",
        "display_name": "Sameeh Ali",
        "star_rating": "FIVE",
        "comment": "The new face of UAE. 🇦🇪",
        "create_time": "2024-02-14T10:40:11.797954Z",
        "update_time": "2024-02-14T10:40:11.797954Z",
        "review_reply": "Thank you so much for your glowing review!",
        "review_reply_update_time": "2024-11-08T13:09:01.759617Z"
      },
      {
        "review_id": "AbFvOqlDCDDdxptda6xsICuyojAXHk9GKTBWCCQAgG5OgNyJCQu0GBOv9xE9uwRlgAbt0zCMC5FRuQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVovqeNAvkVt1CIihq2jLpCsYZxfBiw63RYh1IGyhAPiXk0myjE=s120-c-rp-mo-br100",
        "display_name": "Ritik Mehra",
        "star_rating": "FIVE",
        "comment": "Testing Review By Ritik Mehra - Django Developer (MagicPitch LLC)",
        "create_time": "2024-10-19T10:40:21.400040Z",
        "update_time": "2024-10-19T10:40:21.400040Z",
        "review_reply": null,
        "review_reply_update_time": null
      },
      {
        "review_id": "AbFvOqkYxgzki4QXFMjLHoPxVzBNl-i8hZnteaB3flZbqJdYwqdoARvGgJwoF7GIfK4KLuVQJJv3rA",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVEAvdDe-_UbgeUVGOs35uIHSbAw-LT2mS5i6TjGWeGxuJIUpHQ=s120-c-rp-mo-ba3-br100",
        "display_name": "ahmed shaheen",
        "star_rating": "FIVE",
        "comment": "",
        "create_time": "2024-03-19T20:22:28.897490Z",
        "update_time": "2024-03-19T20:22:28.897490Z",
        "review_reply": null,
        "review_reply_update_time": null
      },
      {
        "review_id": "AbFvOqkFhkIqhswoYaDHzH-uaqL0CoUWEPd7xkB1qrl6aKRcQJSLWotX68_CTj1pUV-SGeMyShGPiQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a/ACg8ocLEO4DQx36vl6Dcroumcd6WXeDq0rTIqJYq1moRQRxsRz0yjQ=s120-c-rp-mo-br100",
        "display_name": "Metro Ceiling Fans",
        "star_rating": "FIVE",
        "comment": "MagicPitch has been a game-changer for our b2b lead generation. Their personalized email strategies and verified contact data have boosted our outreach efficiency and generated qualified leads. Highly recommend them for businesses looking to step up their outreach game.",
        "create_time": "2024-01-29T07:31:49.686680Z",
        "update_time": "2024-01-29T07:31:49.686680Z",
        "review_reply": "Thank you so much for your glowing review! We're thrilled to hear that MagicPitch has made such a positive impact on your business.",
        "review_reply_update_time": "2024-03-04T06:11:50.346361Z"
      },
      {
        "review_id": "AbFvOqlucx5DhJQoihyouLVbsOj2tVEFlA10HCU5T0YZ2U-f3p3MGYFpt5Fem2qb_HKuqFl2MOFq",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjUgTmKcfuuC5wToxcE7CBKmwym4DFYxS9K4HrucS_H4SAWNVxs=s120-c-rp-mo-br100",
        "display_name": "Guide2Success",
        "star_rating": "FOUR",
        "comment": "MagicPitch has been a game-changer for my business! Their approach to outreach is truly unique and effective. What I love most is their personalized touch – from understanding my ideal customer profile to crafting tailored email campaigns, they've helped me connect with prospects in a way that feels genuine and authentic.\n\nMagicPitch team is incredibly dedicated and responsive, always going above and beyond to ensure my success. If you're tired of generic outreach strategies and want something that really works, I highly recommend giving MagicPitch a try. You won't be disappointed!",
        "create_time": "2024-03-04T06:09:20.110800Z",
        "update_time": "2024-03-04T06:09:20.110800Z",
        "review_reply": null,
        "review_reply_update_time": null
      }
    ],
    "entity_uuid": "0b9edbb7-f84c-427b-8f0c-7c3d37905356"
  },
  {
    "info": {
      "account_name": "Info MagicPitch",
      "title": "Magicpitch LLC",
      "region_code": "AE",
      "administrative_area": "Dubai",
      "maps_uri": "https://maps.google.com/maps?cid=16828986524786053041",
      "new_review_uri": "https://search.google.com/local/writereview?placeid=ChIJzWsxMZlDXz4RsU-1mxSSjOk",
      "description": "Magicpitch is an Al powered, Data driven effective outreach Company that specializes in One-to-One Hyper-personalized outreach.\n\nFounded in April 2020, Magicpitch specialized in B2B sales development and provides data-driven, AI-powered hyper-personalized email outreach strategies to help businesses generate qualified leads."
    },
    "reviews": [
      {
        "review_id": "AbFvOqnaAuW3l8WRk5U5EpoSW3D5Gge_LAfihrjfZG8kmAcpF51qNzsvSHM6HWGXrJaa0kdHCzSEQw",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjW0zpyANp8lusdImCJR5-9gXViP3LMOC1HM-ke4_fdc0Bf52Zvs=s120-c-rp-mo-ba3-br100",
        "display_name": "Sameeh Ali",
        "star_rating": "FIVE",
        "comment": "The new face of UAE. 🇦🇪",
        "create_time": "2024-02-14T10:40:11.797954Z",
        "update_time": "2024-02-14T10:40:11.797954Z",
        "review_reply": "Thank you so much for your glowing review!",
        "review_reply_update_time": "2024-11-08T13:09:01.759617Z"
      },
      {
        "review_id": "AbFvOqkFhkIqhswoYaDHzH-uaqL0CoUWEPd7xkB1qrl6aKRcQJSLWotX68_CTj1pUV-SGeMyShGPiQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a/ACg8ocLEO4DQx36vl6Dcroumcd6WXeDq0rTIqJYq1moRQRxsRz0yjQ=s120-c-rp-mo-br100",
        "display_name": "Metro Ceiling Fans",
        "star_rating": "FIVE",
        "comment": "MagicPitch has been a game-changer for our b2b lead generation. Their personalized email strategies and verified contact data have boosted our outreach efficiency and generated qualified leads. Highly recommend them for businesses looking to step up their outreach game.",
        "create_time": "2024-01-29T07:31:49.686680Z",
        "update_time": "2024-01-29T07:31:49.686680Z",
        "review_reply": "Thank you so much for your glowing review! We're thrilled to hear that MagicPitch has made such a positive impact on your business.",
        "review_reply_update_time": "2024-03-04T06:11:50.346361Z"
      },
      {
        "review_id": "AbFvOqlDCDDdxptda6xsICuyojAXHk9GKTBWCCQAgG5OgNyJCQu0GBOv9xE9uwRlgAbt0zCMC5FRuQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVovqeNAvkVt1CIihq2jLpCsYZxfBiw63RYh1IGyhAPiXk0myjE=s120-c-rp-mo-br100",
        "display_name": "Ritik Mehra",
        "star_rating": "FIVE",
        "comment": "Testing Review By Ritik Mehra - Django Developer (MagicPitch LLC)",
        "create_time": "2024-10-19T10:40:21.400040Z",
        "update_time": "2024-10-19T10:40:21.400040Z",
        "review_reply": null,
        "review_reply_update_time": null
      },
      {
        "review_id": "AbFvOqkYxgzki4QXFMjLHoPxVzBNl-i8hZnteaB3flZbqJdYwqdoARvGgJwoF7GIfK4KLuVQJJv3rA",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVEAvdDe-_UbgeUVGOs35uIHSbAw-LT2mS5i6TjGWeGxuJIUpHQ=s120-c-rp-mo-ba3-br100",
        "display_name": "ahmed shaheen",
        "star_rating": "FIVE",
        "comment": "",
        "create_time": "2024-03-19T20:22:28.897490Z",
        "update_time": "2024-03-19T20:22:28.897490Z",
        "review_reply": null,
        "review_reply_update_time": null
      },
      {
        "review_id": "AbFvOqlucx5DhJQoihyouLVbsOj2tVEFlA10HCU5T0YZ2U-f3p3MGYFpt5Fem2qb_HKuqFl2MOFq",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjUgTmKcfuuC5wToxcE7CBKmwym4DFYxS9K4HrucS_H4SAWNVxs=s120-c-rp-mo-br100",
        "display_name": "Guide2Success",
        "star_rating": "FOUR",
        "comment": "MagicPitch has been a game-changer for my business! Their approach to outreach is truly unique and effective. What I love most is their personalized touch – from understanding my ideal customer profile to crafting tailored email campaigns, they've helped me connect with prospects in a way that feels genuine and authentic.\n\nMagicPitch team is incredibly dedicated and responsive, always going above and beyond to ensure my success. If you're tired of generic outreach strategies and want something that really works, I highly recommend giving MagicPitch a try. You won't be disappointed!",
        "create_time": "2024-03-04T06:09:20.110800Z",
        "update_time": "2024-03-04T06:09:20.110800Z",
        "review_reply": null,
        "review_reply_update_time": null
      }
    ],
    "entity_uuid": "2a56731a-b952-4a77-939d-545deb39282f"
  }
]
```

2. Analyse the reviews[*].comment and decide if it required a reply or not. The criterias are:

- is it a postive or negative review. positive review are with reviews[*].star_rating >= 4, and negative are reviews[*].star_rating <= 3
- reviews[*].review_reply = null

3. Use langchain llm with langsmith to reply the reviews, the reply criterias need to use info.description as business background and match the templates below:
   For positive reviews:

- A generic thank-you message expressing gratitude for the positive feedback.
- A personalized response referencing a specific detail from the review (if applicable).
  An invitation to visit again or try a new product/ menu /service.
- If a positive review includes a suggestion for improvement, we need to thank the customer for the feedback and assure them that their input will be considered.

For negative reviews:

- A prompt and apologetic response acknowledging the negative experience.
- An invitation to contact the business directly to discuss the issue further and offering them complimentary services for their next visit.
- A commitment to resolving the problem and improving future experiences.
- ⁠Specific Complaint: If the review mentions a specific issue (e.g., poor service, bad food, etc.), we need to trigger a tailored response addressing that particular concern.

The final api reply response structure will be like following to those reviews need to be replied only:

```json
[
  {
    "reviews": [
      {
        "review_id": "AbFvOqlDCDDdxptda6xsICuyojAXHk9GKTBWCCQAgG5OgNyJCQu0GBOv9xE9uwRlgAbt0zCMC5FRuQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVovqeNAvkVt1CIihq2jLpCsYZxfBiw63RYh1IGyhAPiXk0myjE=s120-c-rp-mo-br100",
        "display_name": "Ritik Mehra",
        "star_rating": "FIVE",
        "comment": "Testing Review By Ritik Mehra - Django Developer (MagicPitch LLC)",
        "create_time": "2024-10-19T10:40:21.400040Z",
        "update_time": "2024-10-19T10:40:21.400040Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      },
      {
        "review_id": "AbFvOqkYxgzki4QXFMjLHoPxVzBNl-i8hZnteaB3flZbqJdYwqdoARvGgJwoF7GIfK4KLuVQJJv3rA",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVEAvdDe-_UbgeUVGOs35uIHSbAw-LT2mS5i6TjGWeGxuJIUpHQ=s120-c-rp-mo-ba3-br100",
        "display_name": "ahmed shaheen",
        "star_rating": "FIVE",
        "comment": "",
        "create_time": "2024-03-19T20:22:28.897490Z",
        "update_time": "2024-03-19T20:22:28.897490Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      },
      {
        "review_id": "AbFvOqlucx5DhJQoihyouLVbsOj2tVEFlA10HCU5T0YZ2U-f3p3MGYFpt5Fem2qb_HKuqFl2MOFq",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjUgTmKcfuuC5wToxcE7CBKmwym4DFYxS9K4HrucS_H4SAWNVxs=s120-c-rp-mo-br100",
        "display_name": "Guide2Success",
        "star_rating": "FOUR",
        "comment": "MagicPitch has been a game-changer for my business! Their approach to outreach is truly unique and effective. What I love most is their personalized touch – from understanding my ideal customer profile to crafting tailored email campaigns, they've helped me connect with prospects in a way that feels genuine and authentic.\n\nMagicPitch team is incredibly dedicated and responsive, always going above and beyond to ensure my success. If you're tired of generic outreach strategies and want something that really works, I highly recommend giving MagicPitch a try. You won't be disappointed!",
        "create_time": "2024-03-04T06:09:20.110800Z",
        "update_time": "2024-03-04T06:09:20.110800Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      }
    ],
    "entity_uuid": "0b9edbb7-f84c-427b-8f0c-7c3d37905356"
  },
  {
    "reviews": [
      {
        "review_id": "AbFvOqlDCDDdxptda6xsICuyojAXHk9GKTBWCCQAgG5OgNyJCQu0GBOv9xE9uwRlgAbt0zCMC5FRuQ",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVovqeNAvkVt1CIihq2jLpCsYZxfBiw63RYh1IGyhAPiXk0myjE=s120-c-rp-mo-br100",
        "display_name": "Ritik Mehra",
        "star_rating": "FIVE",
        "comment": "Testing Review By Ritik Mehra - Django Developer (MagicPitch LLC)",
        "create_time": "2024-10-19T10:40:21.400040Z",
        "update_time": "2024-10-19T10:40:21.400040Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      },
      {
        "review_id": "AbFvOqkYxgzki4QXFMjLHoPxVzBNl-i8hZnteaB3flZbqJdYwqdoARvGgJwoF7GIfK4KLuVQJJv3rA",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjVEAvdDe-_UbgeUVGOs35uIHSbAw-LT2mS5i6TjGWeGxuJIUpHQ=s120-c-rp-mo-ba3-br100",
        "display_name": "ahmed shaheen",
        "star_rating": "FIVE",
        "comment": "",
        "create_time": "2024-03-19T20:22:28.897490Z",
        "update_time": "2024-03-19T20:22:28.897490Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      },
      {
        "review_id": "AbFvOqlucx5DhJQoihyouLVbsOj2tVEFlA10HCU5T0YZ2U-f3p3MGYFpt5Fem2qb_HKuqFl2MOFq",
        "profile_photo_url": "https://lh3.googleusercontent.com/a-/ALV-UjUgTmKcfuuC5wToxcE7CBKmwym4DFYxS9K4HrucS_H4SAWNVxs=s120-c-rp-mo-br100",
        "display_name": "Guide2Success",
        "star_rating": "FOUR",
        "comment": "MagicPitch has been a game-changer for my business! Their approach to outreach is truly unique and effective. What I love most is their personalized touch – from understanding my ideal customer profile to crafting tailored email campaigns, they've helped me connect with prospects in a way that feels genuine and authentic.\n\nMagicPitch team is incredibly dedicated and responsive, always going above and beyond to ensure my success. If you're tired of generic outreach strategies and want something that really works, I highly recommend giving MagicPitch a try. You won't be disappointed!",
        "create_time": "2024-03-04T06:09:20.110800Z",
        "update_time": "2024-03-04T06:09:20.110800Z",
        "review_reply": null,
        "review_reply_update_time": null,
        "agent_reply_draft": "xxxxxxxxx",
        "agent_reply_time": "2024-11-10 00:00:00"
      }
    ],
    "entity_uuid": "2a56731a-b952-4a77-939d-545deb39282f"
  }
]
```
