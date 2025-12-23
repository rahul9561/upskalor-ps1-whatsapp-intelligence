from PIL import Image
import io
import requests

# Placeholder for handwriting validation (replace with your ML model, e.g., CNN)
def is_handwritten_image(image_bytes: bytes) -> bool:
    # Simple heuristic or call your model here
    try:
        img = Image.open(io.BytesIO(image_bytes))
        # Example: check if image has low contrast or handwriting features
        return True  # Replace with real logic
    except:
        return False