"""Command-line interface for sentiment analysis."""

from predict import predict_review

def main():
    """Run the CLI sentiment analyzer."""
    print("\n" + "="*50)
    print("  Amazon Review Sentiment Analyzer (CLI)")
    print("="*50 + "\n")
    
    while True:
        try:
            review = input("📝 Enter your review (or 'quit' to exit):\n> ").strip()
            
            if review.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thank you! Goodbye!\n")
                break
            
            if not review:
                print("⚠️  Please enter a non-empty review.\n")
                continue
            
            sentiment = predict_review(review)
            emoji = "😊" if sentiment == "Positive" else "😞"
            print(f"\n{emoji} Prediction: {sentiment}\n")
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}\n")


if __name__ == "__main__":
    main()