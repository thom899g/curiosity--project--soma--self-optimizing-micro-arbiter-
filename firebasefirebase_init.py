import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Get Firestore client
db = firestore.client()

# Example of a Firestore transaction logging
def log_transaction(tx_hash, intended_profit, actual_profit, gas_used, competitor_interference=False):
    """
    Log a transaction to Firestore for analysis.
    """
    transaction_ref = db.collection('transactions').document(tx_hash)
    transaction_ref.set({
        'intended_profit': intended_profit,
        'actual_profit': actual_profit,
        'gas_used': gas_used,
        'competitor_interference': competitor_interference,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

# Example of reading circuit breaker conditions
def get_circuit_breaker_conditions():
    doc = db.collection('config').document('circuit_breakers').get()
    if doc.exists:
        return doc.to_dict()
    else:
        # Default conditions
        return {
            'max_daily_loss': 0.01,
            'consecutive_fails': 5,
            'gas_spike_threshold': 2.5,
            'competitor_collusion_detected': True
        }