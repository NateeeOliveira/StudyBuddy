from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>StudyBuddy - Learn Smarter</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Poppins', sans-serif;
                background: #0d1117;
                color: #fff;
                line-height: 1.6;
                scroll-behavior: smooth;
            }
            header {
                background: linear-gradient(135deg, #00ffff33, #001f33);
                padding: 60px 20px;
                text-align: center;
            }
            header h1 {
                font-size: 3rem;
                color: #00ffff;
            }
            header p {
                margin-top: 10px;
                font-size: 1.2rem;
                color: #ccc;
            }

            nav {
                background: #010409;
                display: flex;
                justify-content: center;
                gap: 30px;
                padding: 15px;
                border-bottom: 1px solid #1f2937;
            }
            nav a {
                color: #00ffff;
                text-decoration: none;
                font-weight: 600;
                transition: color 0.3s;
            }
            nav a:hover {
                color: #fff;
            }

            .search-container {
                display: flex;
                justify-content: center;
                margin: 40px 0 20px;
            }
            .search-container input {
                padding: 12px 20px;
                width: 80%;
                max-width: 500px;
                border-radius: 30px;
                border: none;
                outline: none;
                font-size: 1rem;
            }

            .flashcard-carousel {
                display: flex;
                overflow-x: auto;
                gap: 20px;
                padding: 20px;
                scroll-snap-type: x mandatory;
                scrollbar-width: none;
            }
            .flashcard-carousel::-webkit-scrollbar { display: none; }
            .flashcard {
                scroll-snap-align: start;
                min-width: 250px;
                background: #1a1a1a;
                border: 2px solid #00ffff;
                padding: 20px;
                border-radius: 10px;
                flex-shrink: 0;
                transition: transform 0.3s;
            }
            .flashcard:hover {
                transform: scale(1.05);
            }

            .button-row {
                display: flex;
                justify-content: center;
                gap: 20px;
                margin: 40px 0;
                flex-wrap: wrap;
            }
            .glow-button {
                background: #00ffff;
                color: #000;
                padding: 12px 30px;
                font-size: 1rem;
                font-weight: 600;
                border: none;
                border-radius: 30px;
                cursor: pointer;
                transition: 0.3s;
                box-shadow: 0 0 10px #00ffff80, 0 0 20px #00ffff40 inset;
            }
            .glow-button:hover {
                transform: scale(1.05);
                box-shadow: 0 0 20px #00ffffcc, 0 0 25px #00ffff66 inset;
            }

            .testimonials {
                background: #111;
                padding: 40px 20px;
                text-align: center;
            }
            .testimonials h2 {
                color: #00ffff;
                margin-bottom: 30px;
            }
            .testimonial {
                max-width: 700px;
                margin: 0 auto 20px;
                font-style: italic;
                color: #ccc;
            }

            .footer {
                background: #000;
                text-align: center;
                padding: 20px;
                font-size: 0.9rem;
                color: #666;
            }

            #scrollBtn {
                position: fixed;
                bottom: 20px;
                right: 20px;
                background: #00ffff;
                color: black;
                border: none;
                border-radius: 50%;
                width: 45px;
                height: 45px;
                font-size: 22px;
                cursor: pointer;
                display: none;
                box-shadow: 0 0 10px #00ffff80;
            }
            #scrollBtn:hover {
                background: #00dddd;
            }

            @media (max-width: 600px) {
                header h1 { font-size: 2rem; }
                nav { flex-direction: column; }
            }
        </style>
    </head>
    <body>

        <header>
            <h1>StudyBuddy</h1>
            <p>Smarter learning, made simple.</p>
        </header>

        <nav>
            <a href="/">Home</a>
            <a href="/study-materials">Study Materials</a>
            <a href="/contact">Contact</a>
        </nav>

        <div class="search-container">
            <input type="text" placeholder="Search topics, notes, or questions...">
        </div>

        <div class="flashcard-carousel">
            <div class="flashcard">📘 What is the powerhouse of the cell?</div>
            <div class="flashcard">🧮 Solve: 2x + 5 = 15</div>
            <div class="flashcard">🌍 Capital of Japan?</div>
            <div class="flashcard">🔬 Define osmosis</div>
            <div class="flashcard">📜 What is the Magna Carta?</div>
        </div>

        <div class="button-row">
            <a href="/study-materials"><button class="glow-button">Explore Materials</button></a>
            <a href="/contact"><button class="glow-button">Join the Community</button></a>
        </div>

        <div class="testimonials">
            <h2>What Students Say</h2>
            <p class="testimonial">"StudyBuddy helped me ace my finals with easy-to-understand flashcards!" – Alex, College Student</p>
            <p class="testimonial">"The interface is clean and super helpful for quick reviews." – Priya, High Schooler</p>
        </div>

        <div class="footer">
            &copy; 2025 StudyBuddy | All Rights Reserved
        </div>

        <button onclick="scrollToTop()" id="scrollBtn" title="Back to Top">&#8679;</button>

        <script>
            const scrollBtn = document.getElementById("scrollBtn");
            window.onscroll = function() {
                if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
                    scrollBtn.style.display = "block";
                } else {
                    scrollBtn.style.display = "none";
                }
            };
            function scrollToTop() {
                window.scrollTo({ top: 0, behavior: 'smooth' });
            }
        </script>

    </body>
    </html>
    '''

@app.route('/study-materials')
def study_materials():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Study Materials</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: #0d1117;
                color: #fff;
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #00ffff;
                margin-bottom: 20px;
            }
            .category {
                margin-top: 30px;
            }
            .category h2 {
                color: #00dddd;
                margin-bottom: 10px;
            }
            .link-box {
                background: #1a1a1a;
                padding: 15px;
                border-left: 4px solid #00ffff;
                border-radius: 8px;
                margin-bottom: 10px;
            }
            .link-box a {
                color: #00ffff;
                font-size: 1.1rem;
                font-weight: 600;
                text-decoration: none;
            }
            .link-box p {
                margin-top: 5px;
                color: #ccc;
                font-size: 0.9rem;
            }
        </style>
    </head>
    <body>
        <h1>Study Materials</h1>
        <div class="category">
            <h2>📘 Physics</h2>
            <div class="link-box">
                <a href="https://www.physicsclassroom.com/Physics-Tutorial" target="_blank">Physics Classroom – Physics Tutorials</a>
                <p>Interactive tutorials and diagrams for high school physics learners.</p>
            </div>
        </div>
        <div class="category">
            <h2>📜 History</h2>
            <div class="link-box">
                <a href="https://www.historyguide.org/guide/guide.html" target="_blank">History Guide – Modern European History</a>
                <p>Detailed lecture series on Western civilization and political thought.</p>
            </div>
        </div>
        <div class="category">
            <h2>🧮 Math</h2>
            <div class="link-box">
                <a href="https://www.sparknotes.com/math/" target="_blank">SparkNotes – Math Study Guides</a>
                <p>Study guides for topics from Algebra to Calculus with summaries and examples.</p>
            </div>
        </div>
    </body>
    </html>
    '''

@app.route('/contact')
def contact():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Contact</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: #0d1117;
                color: #fff;
                padding: 40px 20px;
            }
            h1 {
                color: #00ffff;
                text-align: center;
            }
            .contact-form {
                max-width: 600px;
                margin: 40px auto;
                background: #1a1a1a;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 0 10px #00ffff55;
            }
            .contact-form h2 {
                text-align: center;
                margin-bottom: 20px;
                color: #00ffff;
            }
            .contact-form input,
            .contact-form textarea {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: none;
                border-radius: 8px;
                background: #222;
                color: #fff;
                font-size: 1rem;
            }
            .contact-form button {
                background: #00ffff;
                color: #000;
                padding: 12px 25px;
                border: none;
                border-radius: 30px;
                font-size: 1rem;
                font-weight: bold;
                cursor: pointer;
                width: 100%;
                transition: 0.3s;
                box-shadow: 0 0 15px #00ffff88;
            }
            .contact-form button:hover {
                background: #00dddd;
                transform: scale(1.03);
            }
        </style>
    </head>
    <body>
        <h1>Contact StudyBuddy</h1>
        <div class="contact-form">
            <h2>Send Us a Message</h2>
            <form>
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <textarea rows="5" placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)
