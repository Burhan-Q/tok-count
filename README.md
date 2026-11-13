# tok-cnt

Count tokens in a file or piped text using OpenAI's `tiktoken` encodings.

## Install

```sh
uv sync
```

## Usage

```sh
uv run tok-cnt path/to/file.txt
cat file.txt | uv run tok-cnt
uv run tok-cnt file.txt --model gpt-4
```

Default model is `gpt-5` (`o200k_base`). Any model known to `tiktoken` works.
