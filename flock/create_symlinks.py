from pathlib import Path

def create_symlink(target_path, symlink_path):
    target = Path(target_path).resolve()
    symlink = Path(symlink_path).resolve()
    
    if not symlink.exists():
        symlink.symlink_to(target)
        print(f"Symlink created: {symlink} -> {target}")
    else:
        print(f"Symlink already exists: {symlink}")

# Replace these paths with your actual paths
embedding_pipeline_src = "embedding_pipeline/src"
prompt_engineering_src = "embedding_pipeline/src"
main_flock_src = "flock/src"

# Create symlinks
create_symlink(embedding_pipeline_src, Path(main_flock_src, "embedding_pipeline"))
create_symlink(prompt_engineering_src, Path(main_flock_src, "prompt_engineering"))
