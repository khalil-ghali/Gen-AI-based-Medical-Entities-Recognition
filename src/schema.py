from pydantic import BaseModel, Field, validator
from kor import from_pydantic

class DoctorPatient(BaseModel):
    ID: str = Field(description="The conversation ID")
    name: str = Field(description="The patient's name mentioned in the conversation", default=None)
    age: str = Field(description="The patient's age mentioned in the conversation", default=None)
    condition: str = Field(description="The patient's condition mentioned in the conversation")
    symptoms: str = Field(description="The symptoms that the patient is experiencing and describing")
    precautions: str = Field(description="The precautions advised by the doctor")
    drug: str = Field(description="The drug or medication that the doctor prescribed to the patient")

    @validator("ID")
    def validate_id(cls, value):
        if not value:
            raise ValueError("ID must not be empty")
        return value

class DoctorPatientSchema:
    @staticmethod
    def get_schema():
        schema, validator = from_pydantic(
            DoctorPatient,
            description=(
                "Extract information from the provided doctor-patient conversation, "
                "including: Conversation ID, name, age, condition, symptoms, precautions, and drug."
            ),
            examples=[
                (
                    "n ID: 86 Doctor: Good morning, Mr. Goins. I understand you've been feeling unwell. "
                    "Can you please tell me what symptoms you've been experiencing? Patient: Yes, Doctor. "
                    "I've been vomiting and having diarrhea a lot. I've also been really thirsty and haven't "
                    "been able to keep anything down. Doctor: Thank you for sharing that with me. Based on your "
                    "symptoms, it seems like you might be suffering from gastroenteritis. We'll need to focus on "
                    "rehydrating you and making you feel more comfortable. I would recommend stopping eating solid "
                    "food for a while and trying to take small sips of water. You should also rest and ease back "
                    "into eating when you feel ready. Are there any questions or concerns you have for me? Patient: "
                    "No, that's all great advice. Thank you, Doctor. Doctor: You're welcome. If your symptoms don't "
                    "improve within the next few days or if they worsen, please don't hesitate to come back for a "
                    "follow-up appointment. In the meantime, please make sure to stay hydrated and take it easy.",
                    [{"ID": "86", "name": "Mr. Goins", "age": "50", "condition": "gastroenteritis",
                      "symptoms": "vomiting and diarrhea, thirsty, unable to keep anything down",
                      "precautions": "stop eating solid food, take small sips of water, rest",
                      "drug": "none"}]
                )
            ],
            many=True
        )
        return schema, validator