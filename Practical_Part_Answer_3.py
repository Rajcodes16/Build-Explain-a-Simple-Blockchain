import random

# -------------------------------
# Consensus Mechanism Simulation
# -------------------------------

print("========== Consensus Mechanism Simulation ==========\n")

# -------------------
# 1. Proof of Work (PoW)
# -------------------
print(">>> Proof of Work (PoW) Simulation")

# Mock miners with random computational power
miners = {
    "MinerA": {"power": random.randint(1, 100)},
    "MinerB": {"power": random.randint(1, 100)},
    "MinerC": {"power": random.randint(1, 100)},
}

# Select miner with highest power
pow_winner = max(miners.items(), key=lambda x: x[1]['power'])

print("Miners and their power:")
for name, stats in miners.items():
    print(f"  {name}: Power = {stats['power']}")

print(f"Selected Validator: {pow_winner[0]} (Highest computational power)")
print("Explanation: In PoW, validators (miners) compete by solving cryptographic puzzles. The one with the most power wins.\n")

# -------------------
# 2. Proof of Stake (PoS)
# -------------------
print(">>> Proof of Stake (PoS) Simulation")

# Mock stakers with random stake values
stakers = {
    "StakerA": {"stake": random.randint(1, 100)},
    "StakerB": {"stake": random.randint(1, 100)},
    "StakerC": {"stake": random.randint(1, 100)},
}

# Select staker with highest stake
pos_winner = max(stakers.items(), key=lambda x: x[1]['stake'])

print("Stakers and their stake:")
for name, stats in stakers.items():
    print(f"  {name}: Stake = {stats['stake']}")

print(f"Selected Validator: {pos_winner[0]} (Highest stake)")
print("Explanation: In PoS, validators are chosen based on the amount of tokens they lock (stake) in the network.\n")

# -------------------
# 3. Delegated Proof of Stake (DPoS)
# -------------------
print(">>> Delegated Proof of Stake (DPoS) Simulation")

# Mock delegates
delegates = {
    "Delegate1": {"votes": 0},
    "Delegate2": {"votes": 0},
    "Delegate3": {"votes": 0},
}

# 3 mock voters randomly vote for delegates
voters = ["Voter1", "Voter2", "Voter3"]
print("Voting process:")
for voter in voters:
    selected_delegate = random.choice(list(delegates.keys()))
    delegates[selected_delegate]["votes"] += 1
    print(f"  {voter} voted for {selected_delegate}")

# Select delegate with most votes
dpos_winner = max(delegates.items(), key=lambda x: x[1]['votes'])

print("\nDelegates and their votes:")
for name, stats in delegates.items():
    print(f"  {name}: Votes = {stats['votes']}")

print(f"Selected Validator: {dpos_winner[0]} (Most votes)")
print("Explanation: In DPoS, token holders vote for delegates who validate blocks on their behalf. It is faster and more democratic.\n")

print("========== End of Simulation ==========")
