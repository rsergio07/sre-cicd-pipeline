#!/usr/bin/env python3
import json
import sys
import os

def evaluate_security_results():
    """Evaluate security scan results and fail if critical issues found"""
    critical_issues = 0

    # Check Safety results
    if os.path.exists('app/safety-report.json'):
        with open('app/safety-report.json', 'r') as f:
            try:
                safety_data = json.load(f)
                if isinstance(safety_data, list):
                    critical_issues += len([v for v in safety_data if 'vulnerability' in str(v).lower()])
            except:
                pass

    # Check Bandit results
    if os.path.exists('app/bandit-report.json'):
        with open('app/bandit-report.json', 'r') as f:
            try:
                bandit_data = json.load(f)
                if 'results' in bandit_data:
                    high_issues = [r for r in bandit_data['results'] if r.get('issue_severity') == 'HIGH']
                    critical_issues += len(high_issues)
            except:
                pass

    print(f"Found {critical_issues} critical security issues")

    if critical_issues > 0:
        print("❌ Security scan failed - critical vulnerabilities found")
        sys.exit(1)
    else:
        print("✅ Security scan passed")
        sys.exit(0)

if __name__ == "__main__":
    evaluate_security_results()
