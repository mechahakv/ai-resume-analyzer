✅ STEP 1: Install Prerequisites

Make sure you have:

Node.js (v16 or higher)
Git


Check versions:

node -v
npm -v
git --version

✅ STEP 2: Clone the Repository
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer


(Replace your-username with actual GitHub username)

✅ STEP 3: Install Dependencies
npm install


Wait until installation completes.

If you see vulnerability warnings → you can ignore them for development.

✅ STEP 4: Start Frontend Server
npm start


The app will run at:

http://localhost:3000


Open it in your browser.

🔌 If You Are Backend Developer

Start backend server separately:

cd backend-folder
npm install
npm start


Backend should run on:

http://localhost:5000


Frontend sends POST request to:

http://localhost:5000/analyze

🌿 How To Work In Team (Branch System)

DO NOT push directly to main.

Create a new branch:

git checkout -b feature-yourname


After making changes:

git add .
git commit -m "Added feature"
git push origin feature-yourname

🛑 Common Errors & Fix
Port 3000 already in use:
npm start -- --port 3001

Delete node_modules if broken:
rm -rf node_modules
npm install


(On Windows PowerShell use:)

rd /s /q node_modules
npm install

🧪 If Starting From Scratch (Full Setup Together)
git clone https://github.com/your-username/ai-resume-analyzer.git
cd ai-resume-analyzer
npm install
npm start


Done ✅