$paths = @(
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\azurelogin-agent-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\crewai-agent-test",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\crewai-vm-creation-agent",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\cv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\lang-graph-news-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\langgraph-persistence-streaming-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\langraph-simple-agent-env",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\langraph-terraform-agent-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\open-deep-research-env",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\ragsearch-agent-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\ragtestvenv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\simple-react-agent-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\speechmatics-test-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\terraform-agent-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\travel-mcp-example-venv",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\travel-researcher-agent-env",
    "C:\Users\sunit\AppData\Roaming\jupyter\kernels\travel-researcher-agent-venv"
)

foreach ($p in $paths) {
    if (Test-Path $p) {
        Remove-Item -Recurse -Force $p
        Write-Host "Removed $p"
    } else {
        Write-Host "Not found: $p"
    }
}
