from demo.simulate_attack import simulate_attack
from guardian.features import extract_features
from guardian.detector import detect
from guardian.rewards import calculate_reward


def main():
    print("\n=== KC-IDS Pipeline Start ===\n")

    # 1. Simulate a cloud access event
    event = simulate_attack(unauthorized=True)
    print("Simulated Event:")
    for key, value in event.items():
        print(f"  {key}: {value}")

    # 2. Extract features
    features = extract_features(event)
    print("\nExtracted Features:")
    for key, value in features.items():
        print(f"  {key}: {value}")

    # 3. Detect suspicious activity
    detection = detect(features)
    print("\nDetection Result:")
    for key, value in detection.items():
        print(f"  {key}: {value}")

    # 4. Evaluate outcome and reward
    reward_result = calculate_reward(event, detection)
    print("\nReward Evaluation:")
    for key, value in reward_result.items():
        print(f"  {key}: {value}")

    print("\n=== KC-IDS Pipeline End ===\n")


if __name__ == "__main__":
    main()

