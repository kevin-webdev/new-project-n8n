# n8n Cloud Suite (Render Ready)

Includes:
- n8n (workflow automation)
- MinIO (S3-compatible storage)
- Kokoro TTS (voice generation API)
- NCA Toolkit (worker service)

## Deploy to Render

1. Upload each folder (`n8n`, `minio`, `kokoro-tts`, `nca-toolkit`) as separate services in Render.
2. Set environment variables from `shared.env.example`.
3. Attach disks for MinIO and n8n as needed.
4. Trigger from n8n -> TTS -> worker -> store in MinIO.

Enjoy building automation! 🚀
"# new-project-n8n" 
