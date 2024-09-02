from model_service import ModelService


def main():
    ml_svc = ModelService()
    ml_svc.load_model('xgr_v1')
    pred = ml_svc.predict(
       [10, 9, 134, 46, 16.75, 100, 0, 6, 8]
    )
    print(pred)

if __name__ == '__main__':
    main()