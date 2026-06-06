# Omni-Video-Factory

A powerful video generation and editing framework powered by OmniVideo, ComfyUI workflows, and Hugging Face ZeroGPU.

## Overview

Omni-Video-Factory is an experimental integration that brings together:
- **OmniVideo** - Advanced video generation capabilities
- **ComfyUI** - Flexible workflow management
- **Hugging Face ZeroGPU** - Industrial-grade GPU acceleration

This project supports text-to-video generation, video editing, and is highly compatible with models like:
- LTX-Video
- WanX 2.2
- WanX 2.1

## Features

- 🎬 **Text-to-Video Generation** - Create videos from text prompts
- ✂️ **Video Editing** - Edit and manipulate existing videos
- 🚀 **GPU Acceleration** - Powered by Hugging Face ZeroGPU
- 🔄 **ComfyUI Integration** - Flexible workflow composition
- 🤖 **Multiple Model Support** - Compatible with various video models

## Installation

```bash
git clone https://github.com/rahman32023-glitch/omni-video-factory.git
cd omni-video-factory
pip install -r requirements.txt
```

## Usage

### Basic Video Generation

```python
from omni_video_factory import VideoGenerator

generator = VideoGenerator()
video = generator.generate(prompt="A cat walking through a sunny garden")
video.save("output.mp4")
```

### Using ComfyUI Workflows

```python
from omni_video_factory import WorkflowManager

workflow = WorkflowManager()
# Load and execute custom workflows
result = workflow.execute("path/to/workflow.json")
```

## Requirements

- Python 3.8+
- PyTorch
- CUDA-capable GPU (recommended)
- Hugging Face Account (for ZeroGPU access)

See `requirements.txt` for detailed dependencies.

## Configuration

Create a `.env` file in the root directory:

```env
HUGGINGFACE_TOKEN=your_token_here
MODEL_NAME=omni-video-v1
GPU_DEVICE=0
```

## Project Structure

```
omni-video-factory/
├── src/
│   ├── __init__.py
│   ├── video_generator.py
│   ├── workflow_manager.py
│   └── models/
├── examples/
│   ├── basic_generation.py
│   └── advanced_workflows.py
├── tests/
│   └── test_generation.py
├── requirements.txt
├── .env.example
└── README.md
```

## Examples

### Text-to-Video

```python
from omni_video_factory import VideoGenerator

gen = VideoGenerator()
video = gen.generate(
    prompt="A dog running on a beach at sunset",
    duration=5,
    resolution="1280x720"
)
video.save("dog_beach.mp4")
```

### Video Enhancement

```python
from omni_video_factory import VideoEnhancer

enhancer = VideoEnhancer()
enhanced = enhancer.upscale("input.mp4", scale=2)
enhanced.save("output_upscaled.mp4")
```

## Original Source

This project is based on the Hugging Face Space:
- **Original Space**: [FrameAI4687/Omni-Video-Factory](https://huggingface.co/spaces/FrameAI4687/Omni-Video-Factory)
- **Related Framework**: [SAIS-FUXI/Omni-Video](https://github.com/SAIS-FUXI/Omni-Video)

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is provided as-is. Please check the original source repositories for license information.

## Troubleshooting

### GPU Not Detected
```bash
# Check CUDA availability
python -c "import torch; print(torch.cuda.is_available())"
```

### Out of Memory
- Reduce video resolution
- Lower batch size
- Use a smaller model variant

### Model Download Issues
- Ensure HF_TOKEN is set correctly
- Check internet connection
- Verify disk space availability

## Support

For issues, questions, or feature requests:
1. Check existing [Issues](https://github.com/rahman32023-glitch/omni-video-factory/issues)
2. Create a new issue with detailed description
3. Include error logs and system information

## Roadmap

- [ ] Multi-GPU support
- [ ] Real-time video generation
- [ ] Advanced editing tools
- [ ] Web UI improvements
- [ ] Docker support
- [ ] Model quantization

## Acknowledgments

- Original project: [FrameAI4687](https://huggingface.co/spaces/FrameAI4687)
- Framework: [SAIS-FUXI/Omni-Video](https://github.com/SAIS-FUXI/Omni-Video)
- Powered by [Hugging Face](https://huggingface.co)

---

**Last Updated**: 2026-06-06
