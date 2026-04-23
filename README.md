<!-- ===================== -->
<!-- 💜 UNICORN PENTEST UI -->
<!-- ===================== -->

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff00cc,100:6a00ff&height=200&section=header&text=VULNERABLE%20LOGIN%20LAB&fontSize=38&fontColor=ffffff&animation=fadeIn" width="100%"/>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com/?color=ff00cc&size=18&center=true&vCenter=true&width=600&lines=unicorn-rm+pentest+lab;SQL+Injection+Demo;Web+Security+Practice;Think+like+an+attacker" />
</p>

---

```bash
[ SYSTEM ] unicornOS pentest module v1.0
[ INIT   ] Booting vulnerable environment...
[ LOAD   ] modules: flask, sqlite, auth
[ STATUS ] READY
```
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:ff00cc,100:333399&height=3"/>$ whoami
> unicorn-rm

$ role --current
> Cybersecurity Student

$ lab --start
> vulnerable login system loaded

⚙️ RUN PROJECT
pip install -r requirements.txt
python app.py
> open http://127.0.0.1:5000
> waiting for input...

📸 DEMO
🔐 Login Page
✔ Normal Login
💀 SQL Injection Attack

🧪 ATTACK WALKTHROUGH
[ STEP 1 ] normal login
username: admin
password: admin
> ✔ ACCESS GRANTED
[ STEP 2 ] wrong password
username: admin
password: 123
> ❌ ACCESS DENIED
[ STEP 3 ] SQL injection 💀
username: admin
password: ' OR '1'='1

📜 ATTACK LOG
[LOG] admin/admin        → SUCCESS
[LOG] admin/123          → FAIL
[LOG] admin/' OR '1'='1  → SUCCESS 💀

🛡️ FIX (SECURE MODE)
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (user, password)
)
[ STATUS ] injection blocked ✔

🧬 SKILLS USED
> SQL Injection
> Flask
> SQLite
> Web Security
> Vulnerability Analysis
> Secure Coding
