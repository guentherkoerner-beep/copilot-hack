# Coding with an AI pair programmer

[GitHub Copilot](https://github.com/features/copilot) is your AI pair programmer, built to support you throughout your development experience. As with any new tool, using GitHub Copilot requires learning a few new skills. This project is built to do exactly that, to give you an opportunity to build a project, using the language and tools you typically use, with GitHub Copilot.

> **[Start hacking!](./hackathon.md)**

## Requirements

This project is configured with a [devcontainer](./.devcontainer/devcontainer.json), which can be [run locally](https://code.visualstudio.com/docs/devcontainers/containers) or in a [codespace](https://github.com/features/codespaces). Please refer to the [setup exercise](./content/0-get-started.md) for more information.

The project does assume you are familiar with programming, but is not prescriptive about language or framework choice.

## License 

This project is licensed under the terms of the MIT open source license. Please refer to [MIT](./LICENSE.txt) for the full terms.

## Maintainers 

You can find the list of maintainers in [CODEOWNERS](./.github/CODEOWNERS)

## Support

This project is provided as-is, and may be updated over time. If you have questions, please [open an issue](/issues/new).

## Anthropic-LLM-Workflow

Ein GitHub Actions Workflow (.github/workflows/anthropic-llm.yml) erlaubt, Anthropic-Modelle per Actions UI anzusprechen.
Kurz: Setze das Repository-Secret ANTHROPIC_API_KEY (optional ANTHROPIC_MODEL). In Actions -> "Run workflow" kannst du Prompt, model, temperature, max_tokens, include_files (Komma-getrennt) und commit_response (true/false) angeben. Die Antwort wird als Artifact bereitgestellt und kann optional als Datei ins Repo committed werden.
