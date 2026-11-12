<div dir="rtl">

<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="docs/readme/banner-he.svg" width="100%" alt="TCP Chat: צ'אט לכמה משתמשים עם ניתוח Wireshark"></a>
</p>

<p align="center"><a href="README.md"><img src="docs/readme/lang-en.svg" height="44" alt="Read in English"></a></p>

<p align="center">
  <a href="Summary_Report.pdf"><img src="https://img.shields.io/badge/%D7%93%D7%95%D7%97_%D7%9E%D7%A1%D7%9B%D7%9D-FFD5C9?style=for-the-badge&logo=adobeacrobatreader&logoColor=A8483A" alt="דוח מסכם"></a>
  <a href="packets.pcapng"><img src="https://img.shields.io/badge/%D7%94%D7%A7%D7%9C%D7%98%D7%AA_Wireshark-DAD5FF?style=for-the-badge&logo=wireshark&logoColor=5548C8" alt="הקלטת Wireshark"></a>
  <a href="#run-it"><img src="https://img.shields.io/badge/%D7%94%D7%A8%D7%A6%D7%94-D9F3E7?style=for-the-badge&logo=python&logoColor=1F7350" alt="הרצה"></a>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/github/license/NoyaAdivi/Networking-project?color=DAD5FF&labelColor=5548C8" alt="License"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project/commits/main"><img src="https://img.shields.io/github/last-commit/NoyaAdivi/Networking-project?color=FFD5C9&labelColor=A8483A" alt="Last commit"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/github/languages/top/NoyaAdivi/Networking-project?color=D9F3E7&labelColor=1F7350" alt="Top language"></a>
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/github/repo-size/NoyaAdivi/Networking-project?color=FBD5E0&labelColor=A03A5C" alt="Repo size"></a>
</p>

<h3 align="center">צ'אט שרת ולקוח אמיתי, והוכחה לכל בייט שעובר ברשת.</h3>

<p align="center">
  שרת TCP ולקוחות עם ממשק גרפי שמדברים בזמן אמת, עם הודעות פרטיות ורשימת מחוברים,<br>ועוד <b>הקלטת Wireshark</b> שמראה את לחיצת היד, את התוכן ואת הסגירה. פרויקט בקורס רשתות תקשורת.
</p>

<table align="center">
  <tr>
    <td align="center" width="25%"><a href="#run-it"><b>🔌 TCP</b></a><br><sub>פורט 12345</sub></td>
    <td align="center" width="25%"><a href="#how-it-works"><b>👥 כמה</b></a><br><sub>לקוחות במקביל</sub></td>
    <td align="center" width="25%"><a href="#how-it-works"><b>🧵 1</b></a><br><sub>תהליכון לכל לקוח</sub></td>
    <td align="center" width="25%"><a href="packets.pcapng"><b>🦈 .pcapng</b></a><br><sub>הקלטת תעבורה אמיתית</sub></td>
  </tr>
</table>

<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="docs/readme/showcase-he.png" width="100%" alt="TCP Chat: צ'אט לכמה משתמשים עם ניתוח Wireshark"></a>
</p>

<a name="highlights"></a>
<p align="center"><a href="#how-it-works"><img src="docs/readme/highlights-he.svg" width="100%" alt="מה מיוחד בו"></a></p>

<table>
  <tr valign="top">
    <td width="33%"><p><b>💬 צ'אט מלא</b></p><ul><li><b>הודעה לכולם</b> בבת אחת</li><li><b>הודעות פרטיות</b> עם <code>/dm</code></li><li><b>מי מחובר</b> עם <code>/users</code></li></ul></td>
    <td width="33%"><p><b>🧵 אסינכרוני מההתחלה</b></p><ul><li><b>שרת:</b> תהליכון נפרד לכל לקוח</li><li><b>לקוח:</b> קבלת ההודעות רצה ברקע</li><li><b>הממשק לא נתקע</b> כשמגיעות הודעות</li></ul></td>
    <td width="33%"><p><b>🦈 רואים את זה ברשת</b></p><ul><li><b>לחיצת יד משולשת</b> וסגירה מסודרת</li><li><b>מספרי רצף ו־ACK</b> בהקלטה אמיתית</li><li><b>מחברת עם הסברים</b> לניתוח TCP/IP</li></ul></td>
  </tr>
</table>

<a name="how-it-works"></a>
<p align="center"><a href="#tech-stack"><img src="docs/readme/how-it-works-he.svg" width="100%" alt="איך זה עובד"></a></p>

```mermaid
sequenceDiagram
  participant A as 🧑 לקוח A
  participant S as 🖥️ שרת
  participant B as 👩 לקוח B
  A->>S: SYN · SYN-ACK · ACK (התחברות)
  B->>S: SYN · SYN-ACK · ACK (התחברות)
  A->>S: /users
  S-->>A: Noya, Amit
  A->>S: שלום לכולם!
  S-->>B: [A] שלום לכולם!
  A->>S: /dm Noya נתראה ב־8
  S-->>B: [פרטי מ־A] נתראה ב־8
  A->>S: FIN (התנתקות)
```

| פקודה | מה היא עושה |
|---|---|
| `/users` | מציגה מי מחובר |
| `/dm <username> <message>` | שולחת הודעה פרטית |
| טקסט חופשי | נשלח לכולם |

> [!NOTE]
> הכול רץ בזיכרון, אין צורך במסד נתונים.

<a name="tech-stack"></a>
<p align="center"><a href="#run-it"><img src="docs/readme/tech-stack-he.svg" width="100%" alt="טכנולוגיות"></a></p>

<p align="center">
  <a href="https://www.python.org"><img src="https://img.shields.io/badge/Python-CFE6FA?style=for-the-badge&logo=python&logoColor=3F6D9F" alt="Python"></a>
  <a href="https://docs.python.org/3/library/socket.html"><img src="https://img.shields.io/badge/Sockets-DAD5FF?style=for-the-badge&logo=python&logoColor=5548C8" alt="Sockets"></a>
  <a href="https://docs.python.org/3/library/threading.html"><img src="https://img.shields.io/badge/Threading-FBD5E0?style=for-the-badge&logo=python&logoColor=A03A5C" alt="Threading"></a>
  <a href="https://docs.python.org/3/library/tkinter.html"><img src="https://img.shields.io/badge/Tkinter-D9F3E7?style=for-the-badge&logo=python&logoColor=1F7350" alt="Tkinter"></a>
  <a href="https://www.wireshark.org"><img src="https://img.shields.io/badge/Wireshark-FFD5C9?style=for-the-badge&logo=wireshark&logoColor=A8483A" alt="Wireshark"></a>
  <a href="https://jupyter.org"><img src="https://img.shields.io/badge/Jupyter-FFD5C9?style=for-the-badge&logo=jupyter&logoColor=A8483A" alt="Jupyter"></a>
</p>

<a name="run-it"></a>
<p align="center"><a href="#contact"><img src="docs/readme/run-it-he.svg" width="100%" alt="הרצה"></a></p>

צריך **Python 3** (בלי חבילות נוספות) ואת [Wireshark](https://www.wireshark.org) בשביל הניתוח.

1. **מפעילים את השרת** (מאזין לפורט 12345):
   ```bash
   python3 server.py
   ```
2. **מפעילים לקוח** בכל חלון טרמינל נוסף:
   ```bash
   python3 client_gui.py
   ```
3. בחלון: בוחרים שם משתמש ייחודי, כתובת `127.0.0.1`, פורט `12345`, ולוחצים **Connect**.

**🦈 להקליט:** על ממשק ה־**Loopback**, עם הסינון `tcp.port == 12345` (או `ip.addr == 127.0.0.1 && tcp.port == 12345`).

<details>
<summary><b>📂 הקבצים</b></summary>

| קובץ | מה הוא |
|---|---|
| [`server.py`](server.py) | שרת TCP שמנהל חיבורים ומעביר הודעות |
| [`client_gui.py`](client_gui.py) | לקוח עם ממשק גרפי |
| [`Summary_Report.pdf`](Summary_Report.pdf) | סיכום מלא של הפרויקט והארכיטקטורה |
| [`packets.pcapng`](packets.pcapng) | הקלטת Wireshark של התעבורה |
| [`group06_ttp_chat_input.csv`](group06_ttp_chat_input.csv) | נתוני הקלט של הצ'אט |
| [`raw_tcp_ip_notebook_fallback_annotated-v1.ipynb`](raw_tcp_ip_notebook_fallback_annotated-v1.ipynb) | מחברת עם ניתוח TCP/IP מוסבר |
</details>

<sub>🤖 נעזרנו בכלי AI רק ללמידה, לתכנון ולתיעוד. את כל הקוד בדקנו, הבנו והתאמנו בעצמנו.</sub>

<a name="contact"></a>
<p align="center"><a href="https://www.linkedin.com/in/noya-adivi/"><img src="docs/readme/footer-he.svg" width="100%" alt="נוצר על ידי נויה אדיבי"></a></p>

<p align="center">
  <a href="https://github.com/NoyaAdivi/Networking-project"><img src="https://img.shields.io/badge/%D7%9C%D7%A4%D7%A8%D7%95%D7%99%D7%A7%D7%98-FFD5C9?style=for-the-badge&logo=github&logoColor=A8483A" alt="לפרויקט"></a>
  <a href="https://www.linkedin.com/in/noya-adivi/"><img src="https://img.shields.io/badge/LinkedIn-DAD5FF?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0iIzU1NDhDOCIgZD0iTTIwLjQ1IDIwLjQ1aC0zLjU2di01LjU3YzAtMS4zMy0uMDMtMy4wNC0xLjg1LTMuMDQtMS44NiAwLTIuMTQgMS40NS0yLjE0IDIuOTR2NS42N0g5LjM1VjloMy40MXYxLjU2aC4wNWMuNDgtLjkgMS42NC0xLjg1IDMuMzctMS44NSAzLjYgMCA0LjI3IDIuMzcgNC4yNyA1LjQ2djYuMjh6TTUuMzQgNy40M2EyLjA2IDIuMDYgMCAxIDEgMC00LjEzIDIuMDYgMi4wNiAwIDAgMSAwIDQuMTN6TTcuMTIgMjAuNDVIMy41NlY5aDMuNTZ2MTEuNDV6TTIyLjIyIDBIMS43N0MuNzkgMCAwIC43NyAwIDEuNzN2MjAuNTRDMCAyMy4yMy43OSAyNCAxLjc3IDI0aDIwLjQ1Yy45OCAwIDEuNzgtLjc3IDEuNzgtMS43M1YxLjczQzI0IC43NyAyMy4yIDAgMjIuMjIgMHoiLz48L3N2Zz4=" alt="LinkedIn"></a>
  <a href="https://noyaadivi.github.io/noya-website"><img src="https://img.shields.io/badge/%D7%AA%D7%99%D7%A7_%D7%A2%D7%91%D7%95%D7%93%D7%95%D7%AA-D9F3E7?style=for-the-badge&logo=githubpages&logoColor=1F7350" alt="תיק עבודות"></a>
  <a href="https://github.com/NoyaAdivi"><img src="https://img.shields.io/badge/%D7%A2%D7%95%D7%93_%D7%A4%D7%A8%D7%95%D7%99%D7%A7%D7%98%D7%99%D7%9D-FBD5E0?style=for-the-badge&logo=github&logoColor=A03A5C" alt="עוד פרויקטים"></a>
</p>

</div>
