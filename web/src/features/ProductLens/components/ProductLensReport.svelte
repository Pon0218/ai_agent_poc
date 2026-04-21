<script lang="ts">
	import { marked } from 'marked';
	import ContentCopyIcon from '@material-symbols/svg-400/outlined/content_copy.svg?component';
	import MarkdownCopyIcon from '@material-symbols/svg-400/outlined/markdown_copy.svg?component';
	import PictureAsPdfIcon from '@material-symbols/svg-400/outlined/picture_as_pdf.svg?component';

	let { markdown, onReset }: { markdown: string; onReset: () => void } = $props();

	const renderedHtml = $derived(marked.parse(markdown) as string);

	let reportEl = $state<HTMLElement | null>(null);
	let copiedPlain = $state(false);
	let copiedMarkdown = $state(false);

	async function copyPlainText() {
		const text = reportEl?.innerText ?? markdown;
		await navigator.clipboard.writeText(text);
		copiedPlain = true;
		setTimeout(() => (copiedPlain = false), 1500);
	}

	async function copyMarkdown() {
		await navigator.clipboard.writeText(markdown);
		copiedMarkdown = true;
		setTimeout(() => (copiedMarkdown = false), 1500);
	}

	function downloadPdf() {
		const content = reportEl?.innerHTML ?? '';
		const win = window.open('', '_blank');
		if (!win) return;

		const style = win.document.createElement('style');
		style.textContent = `
      *, *::before, *::after { box-sizing: border-box; }
      body { font-family: Georgia, 'Times New Roman', serif; max-width: 720px; margin: 0 auto; padding: 2rem 2.5rem; color: #111; line-height: 1.7; font-size: 15px; }
      h1 { font-size: 1.8rem; font-weight: 700; margin: 0 0 0.75em; line-height: 1.2; }
      h2 { font-size: 1.35rem; font-weight: 600; margin: 1.75em 0 0.5em; }
      h3 { font-size: 1.1rem; font-weight: 600; margin: 1.25em 0 0.4em; }
      h4 { font-size: 1rem; font-weight: 600; margin: 1em 0 0.3em; }
      p { margin: 0.6em 0 0.8em; }
      ul, ol { padding-left: 1.5em; margin: 0.5em 0 0.8em; }
      li { margin: 0.3em 0; }
      strong { font-weight: 700; }
      em { font-style: italic; }
      hr { border: none; border-top: 1px solid #ddd; margin: 1.5em 0; }
      blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 1em; color: #444; }
      code { background: #f3f3f3; padding: 0.15em 0.4em; border-radius: 3px; font-family: 'Courier New', monospace; font-size: 0.875em; }
      pre { background: #f3f3f3; padding: 1em; border-radius: 5px; overflow-x: auto; margin: 1em 0; }
      pre code { background: none; padding: 0; }
      table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: 0.9em; }
      th { background: #f3f3f3; font-weight: 600; text-align: left; padding: 0.5em 0.75em; border: 1px solid #ddd; }
      td { padding: 0.45em 0.75em; border: 1px solid #ddd; }
      @media print { body { padding: 0; } a { color: inherit; text-decoration: none; } }
    `;
		win.document.head.appendChild(style);
		win.document.title = 'Product Report';
		win.document.body.innerHTML = content;
		win.focus();
		setTimeout(() => win.print(), 250);
	}
</script>

<svelte:head>
	<style>
		@media print {
			body > * {
				display: none !important;
			}
			.print-report {
				display: block !important;
				position: fixed;
				inset: 0;
				padding: 2rem;
				background: white;
				color: #111 !important;
			}
			.print-report * {
				color: inherit !important;
				background: transparent !important;
			}
			.print-toolbar {
				display: none !important;
			}
		}
	</style>
</svelte:head>

<div class="w-full px-4 py-6 md:px-8">
	<!-- Toolbar -->
	<div class="print-toolbar mb-4 flex items-center justify-between gap-3">
		<button
			onclick={onReset}
			class="cursor-pointer rounded-lg border border-s-stroke px-3 py-1.5 text-xs text-s-sub-headline transition-all hover:border-s-button hover:text-s-headline active:scale-95"
		>
			← New Analysis
		</button>
		<div class="flex gap-3">
			<button
				onclick={copyPlainText}
				title="複製原文"
				aria-label="複製原文"
				class="flex size-8 cursor-pointer items-center justify-center rounded-md border transition-all active:scale-95"
				class:border-green-400={copiedPlain}
				class:opacity-100={copiedPlain}
				class:border-s-button={!copiedPlain}
				class:opacity-50={!copiedPlain}
				class:hover:opacity-100={!copiedPlain}
			>
				<ContentCopyIcon
					class="size-5 {copiedPlain ? 'fill-green-400' : 'fill-s-button'}"
				/>
			</button>
			<button
				onclick={copyMarkdown}
				title="複製 Markdown"
				aria-label="複製 Markdown"
				class="flex size-8 cursor-pointer items-center justify-center rounded-md border transition-all active:scale-95"
				class:border-green-400={copiedMarkdown}
				class:opacity-100={copiedMarkdown}
				class:border-s-button={!copiedMarkdown}
				class:opacity-50={!copiedMarkdown}
				class:hover:opacity-100={!copiedMarkdown}
			>
				<MarkdownCopyIcon
					class="size-5 {copiedMarkdown ? 'fill-green-400' : 'fill-s-button'}"
				/>
			</button>
			<button
				onclick={downloadPdf}
				title="下載 PDF"
				aria-label="下載 PDF"
				class="flex size-8 cursor-pointer items-center justify-center rounded-md border border-s-button opacity-50 transition-all hover:opacity-100 active:scale-95"
			>
				<PictureAsPdfIcon class="size-5 fill-s-button" />
			</button>
		</div>
	</div>

	<!-- Report Content -->
	<div bind:this={reportEl} class="print-report mx-auto prose prose-sm max-w-180 md:prose-base">
		<!-- eslint-disable-next-line svelte/no-at-html-tags -->
		{@html renderedHtml}
	</div>
</div>
