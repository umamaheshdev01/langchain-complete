from deepagents.backends import StateBackend, FilesystemBackend, CompositeBackend
from deepagents.middleware import FilesystemMiddleware
from deepagents.middleware import MemoryMiddleware, SkillsMiddleware, SummarizationMiddleware
from pathlib import Path
from agent_helpers.model import model
from langchain.agents.middleware import TodoListMiddleware,ModelRetryMiddleware, ToolRetryMiddleware
from langchain.agents.middleware import PIIMiddleware,HumanInTheLoopMiddleware


humanloop_middlware = HumanInTheLoopMiddleware(
      interrupt_on={
        "write_file": True,
    }
)

todo = TodoListMiddleware()
tool_retry = ToolRetryMiddleware()
model_retry = ModelRetryMiddleware()


protection_middleware = PIIMiddleware("email")


base_dir = Path(__file__).parent
workspace = base_dir / "workspace"
summary_dir = base_dir / "summary"
skills_dir = base_dir / "skills"
memory_dir = base_dir / "memory"

for d in (workspace, summary_dir, skills_dir, memory_dir):
    d.mkdir(exist_ok=True)


memory_file = memory_dir / "AGENTS.md"
if not memory_file.exists():
    memory_file.write_text(
        "# Agent Memory\n\n"
        "## User Preferences\n\n(none yet)\n\n"
        "## Learned Facts\n\n(none yet)\n"
    )


file_sys_temp_middleware = FilesystemMiddleware(backend=StateBackend())


shared_backend = CompositeBackend(
    default=FilesystemBackend(root_dir=str(workspace), virtual_mode=True),
    routes={
        "/skills/": FilesystemBackend(root_dir=str(skills_dir), virtual_mode=True),
        "/memory/": FilesystemBackend(root_dir=str(memory_dir), virtual_mode=True),
    },
)

file_sys_per_middleware = FilesystemMiddleware(backend=shared_backend)

summary_middlware = SummarizationMiddleware(
    model=model,
    trigger=("tokens", 1000),
    keep=("messages", 3),
    backend=FilesystemBackend(root_dir=str(summary_dir), virtual_mode=True),
)


skills_middleware = SkillsMiddleware(
    backend=shared_backend,
    sources=["/skills/"],
)


memory_middleware = MemoryMiddleware(
    backend=shared_backend,
    sources=["/memory/AGENTS.md"],
)
