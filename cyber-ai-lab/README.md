# Cyber AI Lab — experimental Termux extension

This is a non-invasive starter kit for the existing Termux fork. It does not change the app ID, bootstrap, Gradle build, signing, or upstream application code.

## Setup (inside Termux)
```bash
cd ~
git clone -b feature/cyber-ai-lab https://github.com/Metmetza88/termux-app.git
bash termux-app/cyber-ai-lab/setup.sh
python ~/cyber-ai-lab/lab.py
```

Includes Python, Git, OpenSSH, curl, nano, Nmap and a localhost-only Python exercise. Only test hosts you own or have explicit permission to test.

## AI design (not yet implemented)
Add an opt-in assistant with a configurable HTTPS API endpoint and an API key entered at runtime, never committed or embedded in an APK. AI should propose commands but not execute them without confirmation.

## Build APK
Go to GitHub Actions > Build on this fork. The upstream workflow builds on pushes to master, so this feature branch may need a pull request to master to trigger a build. Once the workflow succeeds, download the APK from its Artifacts section. Do not merge before reviewing and testing.

## Signing and compatibility
Upstream debug builds use a publicly known test key. Do not distribute as a production-signed app. APKs from other signing sources may conflict with installed Termux and plugins. Back up before replacing. A separate Android package ID requires a custom bootstrap and further upstream modifications.
