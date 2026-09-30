from flask import Flask, request

app = Flask(__name__)

correct_pin = "1234"

attempts = 0
blocked = False


@app.route("/", methods=["GET", "POST"])
def atm():

    global attempts, blocked

    message = ""

    if request.method == "POST":

        if blocked:
            message = "Account Blocked. Maximum attempts exceeded."

        else:

            pin = request.form["pin"]

            attempts += 1

            if pin == correct_pin:

                message = "Login Successful"

                attempts = 0

            else:

                if attempts < 3:
                    message = "Wrong PIN. Try Again."
                else:
                    message = "Account Blocked. Maximum attempts exceeded."
                    blocked = True

    # ---------------- HTML + CSS ----------------

    html = f"""
    <!DOCTYPE html>

    <html>

    <head>

        <title>ATM Login</title>

        <style>

            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: Arial, sans-serif;
                background: #e8f0f7;

                height: 100vh;

                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .atm-box {{
                width: 400px;

                background: white;

                padding: 40px;

                border-radius: 18px;

                text-align: center;

                box-shadow: 0 10px 30px rgba(0,0,0,0.15);
            }}

            .icon {{
                font-size: 60px;
                margin-bottom: 15px;
            }}

            h1 {{
                color: #1f2937;
                margin-bottom: 10px;
            }}

            .subtitle {{
                color: #6b7280;
                margin-bottom: 25px;
            }}

            input {{
                width: 100%;

                padding: 14px;

                font-size: 20px;

                text-align: center;

                border: 2px solid #d1d5db;

                border-radius: 8px;

                margin-bottom: 15px;

                outline: none;
            }}

            input:focus {{
                border-color: #2563eb;
            }}

            button {{
                width: 100%;

                padding: 14px;

                background: #2563eb;

                color: white;

                border: none;

                border-radius: 8px;

                font-size: 17px;

                font-weight: bold;

                cursor: pointer;
            }}

            button:hover {{
                background: #1d4ed8;
            }}

            button:disabled {{
                background: #6b7280;
                cursor: not-allowed;
            }}

            .message {{
                margin-top: 20px;

                padding: 15px;

                border-radius: 8px;

                font-weight: bold;
            }}

            .success {{
                background: #dcfce7;
                color: #15803d;
            }}

            .wrong {{
                background: #fef3c7;
                color: #b45309;
            }}

            .blocked {{
                background: #fee2e2;
                color: #b91c1c;
            }}

        </style>

    </head>


    <body>

        <div class="atm-box">

            <div class="icon">
                🏧
            </div>

            <h1>
                ATM Login
            </h1>

            <p class="subtitle">
                Enter your 4-digit PIN
            </p>


            <form method="POST">

                <input
                    type="password"
                    name="pin"
                    placeholder="Enter PIN"
                    maxlength="4"
                    required
                >

                {
                    '<button type="submit">Login</button>'
                    if not blocked
                    else
                    '<button type="button" disabled>Account Blocked</button>'
                }

            </form>


            {
                f'<div class="message success">✅ {message}</div>'
                if message == "Login Successful"
                else
                f'<div class="message blocked">🔒 {message}</div>'
                if "Blocked" in message
                else
                f'<div class="message wrong">⚠️ {message}</div>'
                if message
                else
                ''
            }

        </div>

    </body>

    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)