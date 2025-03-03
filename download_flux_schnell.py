from huggingface_hub import snapshot_download

# 指定模型仓库
repo_id = "black-forest-labs/FLUX.1-schnell"
# 指定本地保存路径
local_dir = "/root/autodl-tmp/models/black-forest-labs/FLUX.1-schnell"  # 替换为你想要保存的文件夹路径
# 指定要跳过的文件
ignore_patterns = ["text_encoder_2/*]

# 下载模型，跳过指定文件
snapshot_download(
    repo_id=repo_id,
    local_dir=local_dir,
    ignore_patterns=ignore_patterns,
    local_dir_use_symlinks=False  # 确保文件直接下载而不是符号链接
)

print(f"模型已下载到 {local_dir}，跳过了 flux1-schnell.safetensors")
