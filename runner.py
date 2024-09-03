from model_service import ModelService
from config import settings


def main():
    ml_svc = ModelService()
    ml_svc.load_model(settings.model_name)
    pred = ml_svc.predict(
       [10, 9, 134, 46, 16.75, 100, 0, 6, 8]
    )
    print(pred)

if __name__ == '__main__':
    main()