# 🎉Calculator🎉  
====================================  
🚀 A cheeky little command-line calculator with attitude.  
🧮 It adds, subtracts, multiplies, divides, and even does exponents!  
😂 But don’t divide by zero — it *will* sass you.  

---

## ✨ Features
- ➕ Addition  
- ➖ Subtraction  
- ✖️ Multiplication  
- ➗ Division (with a roast if you try zero 🙃)  
- 🔼 Exponentiation  

And yes… it makes you wait with a dramatic "calculating..." animation.  
Because math should be suspenseful. 😏   
  
---  
  
## 🛠 Requirements  
- Python 3.x (≥ 3.6 recommended)  
- That’s it. No fancy libraries, just you and math.  

---

## ▶️ How to Run  
1. Save the script as `calculator.py`.   
2. Open a terminal and run:    
  
```bash
python calculator.py
```
## Decision Tree

Start  
---└── Input number1  
------└── Input number2  
-----------└── Choose operation (+, -, *, /, ^)  
------------------├── '+' → Add → Show result → Calculate again? (y/n)  
------------------├── '-' → Subtract → Show result → Calculate again? (y/n)  
------------------├── '*' → Multiply → Show result → Calculate again? (y/n)  
------------------├── '/' → Divide  
------------------│        ├── number2 ≠ 0 → Show result → Calculate again? (y/n)  
------------------│        └── number2 = 0 → Show error → Calculate again? (y/n)  
------------------├── '^' → Exponent → Show result → Calculate again? (y/n)  
------------------└── Invalid input → Show error → Loop back  
