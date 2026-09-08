# The Software Engineer Reborn

A vision of human–AI collaboration, by John Lee.

[View the slides](https://leej3.github.io/software-engineer-reborn/).

## Edit and preview

The editable deck is [slides/index.qmd](slides/index.qmd).
Each `##` heading starts a slide; `::: {.notes}` blocks contain speaker notes.
Press **S** in the presentation to open the speaker view.
The notes are included in the published HTML.

Install [Pixi](https://pixi.sh), then run from the repository root:

```bash
pixi install --locked
pixi run slides-preview
```

Open the local URL printed by Quarto.
The preview updates as you save edits.
Quarto and the formatting tools are managed by `pixi.toml` and `pixi.lock`.

```bash
pixi run slides-format
pixi run slides-build
```

The rendered deck is written to `slides/_site/`.
Its appearance and presentation options are configured in [slides/_quarto.yml](slides/_quarto.yml).
The deck uses Reveal.js with a 16:9 layout and speaker notes.

## Publish

Push changes to `main` to render and deploy through GitHub Actions.
Pull requests build the slides without deploying them.
GitHub Pages uses the **GitHub Actions** publishing source.
Only the rendered `slides/_site/` directory is deployed.

The original planning documents remain in `docs/`, `talk-concepts/`, and `talk-candidates/`.
The professional-identity candidate has moved to `slides/index.qmd`, which is now the source to edit.

## License

Copyright © 2026 John Lee.
Except where otherwise indicated, the original material in this repository is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
See [LICENSE](LICENSE) for the full terms.
Suggested attribution: “The Software Engineer Reborn” by John Lee, with a link to this repository and the license.
Third-party materials retain their respective licenses.
