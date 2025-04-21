from langchain.llms import HuggingFaceHub
from langchain import create_extraction_chain
from schema import DoctorPatientSchema

class EntityExtraction:
    def __init__(self, huggingface_api_token):
        self.huggingface_api_token = huggingface_api_token
        self.llm = self._initialize_llm()

    def _initialize_llm(self):
        repo_id = "tiiuae/falcon-7b-instruct"
        return HuggingFaceHub(
            huggingfacehub_api_token=self.huggingface_api_token,
            repo_id=repo_id,
            model_kwargs={"temperature": 0.01, "max_new_tokens": 700}
        )

    def extract_entities(self, texts):
        schema, _ = DoctorPatientSchema.get_schema()
        chain = create_extraction_chain(
            llm=self.llm,
            schema=schema,
            encoder_or_encoder_class="json"
        )
        extracted_data = []
        for text in texts:
            result = chain.run(text.page_content)
            extracted_data.append(result["data"])
        return extracted_data