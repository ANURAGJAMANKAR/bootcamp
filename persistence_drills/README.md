# Persistence Learning Path: File & Database Systems

**Author: Anurag**

A comprehensive hands-on guide to mastering data persistence in Python, covering everything from basic file serialization to advanced database engineering patterns. This curriculum emphasizes practical learning through progressive exercises that build real-world skills.

## 🎯 Learning Philosophy

These drills are designed for active learning — **do not delegate to LLMs**. Each exercise builds foundational understanding through hands-on implementation. Like physical drills, repetition and practice develop muscle memory for persistence patterns you'll use throughout your career.

---

## 📚 Prerequisites & Essential Concepts

### Core Database Concepts

Before diving into the exercises, I have written about these fundamental concepts. 

#### 🗃️ Understanding Transactions and ACID Properties

**What are transactions?**  
A transaction is a group of operations that are executed as a single unit. Either all operations succeed, or none do. This ensures data safety and consistency.

**Real-life Example**: Transferring ₹1,000 from your savings to your friend's account:
1. ₹1,000 is deducted from your savings  
2. ₹1,000 is added to your friend's account  

If step 2 fails but step 1 succeeded, your money would disappear! Transactions ensure both steps succeed or both are rolled back.

**What are ACID Properties?**  
ACID ensures transactions are processed reliably:
- **A – Atomicity**: Everything in a transaction must succeed. If one thing fails, everything is rolled back.
- **C – Consistency**: Data must stay valid before and after the transaction.
- **I – Isolation**: Multiple transactions don't affect each other.
- **D – Durability**: Once complete, data is saved even if the system crashes.

---

#### 🤔 Self-Assessment Questions

**Suppose you don't have transactions. Is that system useful? Why?**  
Without transactions, there's a risk of partial updates leading to inconsistent data. However, some systems still work:
- ✅ **Useful**: Reading config files, logging systems, simple lookups  
- ❌ **Problems**: Partial updates leave corrupted/incomplete data

**What properties does your file system have?**
- **Durability**: Data remains after restart  
- **Basic atomicity**: Can replace whole files, but not partial contents  
- ❌ **No consistency or isolation**

**What if you don’t have "A" (Atomicity)?**
- ❌ **Problem**: Broken or partial data  
- ✅ **Okay**: Logs, metrics, analytics  
- **Example**: One line missed in log is fine, but not in a banking transaction

**What if you don’t have "C" (Consistency)?**
- ❌ **Problem**: Inconsistent or invalid data  
- ✅ **Okay**: Eventual consistency, data migration scenarios  
