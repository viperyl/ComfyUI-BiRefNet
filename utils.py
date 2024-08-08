import os


def check_download_model(model_path, repo_id="ViperYX/BiRefNet"):
    if not os.path.exists(model_path):
        folder_path = os.path.dirname(model_path)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_name = os.path.basename(model_path)
        print(f"Downloading BiRefNet model to: {model_path}")
        from huggingface_hub import snapshot_download
        snapshot_download(repo_id=repo_id,
                        allow_patterns=[f"*{file_name}*"],
                        local_dir=folder_path,
                        local_dir_use_symlinks=False)
        return True
    return False
