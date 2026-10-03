# ========================================================
# 💻 TOPIC 1: PYTHON FUNCTIONS (REUSABLE CODE BLOCK)
# ========================================================

def check_coupon(student_name, coupon_code):
    print("\n⏳ Validating coupon code in system...")
    
    if coupon_code == "WELCOME10":
        print(f"✅ Success: 10% Discount applied for {student_name}!")
    else:
        print(f"❌ Invalid: Coupon code '{coupon_code}' does not exist.")

if __name__ == "__main__":
    print("--- Coupon Verification System ---")
    
    # Testing the function with different arguments
    check_coupon("Priyanka Kumari", "WELCOME10")
    check_coupon("Rahul Kumar", "WRONG50")