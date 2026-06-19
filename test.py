from utils.predictor import predict_drugs_for_cell

results = predict_drugs_for_cell(
    "ACH-000769"
)

print(results.head())