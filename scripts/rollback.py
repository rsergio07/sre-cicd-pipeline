#!/usr/bin/env python3
import argparse

def rollback_deployment(environment, reason):
    """Simulate rollback to previous version"""
    print(f"🔄 Initiating rollback for {environment} environment")
    print(f"   Reason: {reason}")

    print("   Finding previous successful deployment...")
    print("   Rolling back to previous version...")
    print("   Verifying rollback...")

    print("✅ Rollback completed successfully")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", required=True)
    parser.add_argument("--reason", required=True)
    args = parser.parse_args()

    rollback_deployment(args.environment, args.reason)
