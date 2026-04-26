<script lang="ts">
	import ContentCopyIcon from '@material-symbols/svg-400/outlined/content_copy.svg?component';
	import MarkdownCopyIcon from '@material-symbols/svg-400/outlined/markdown_copy.svg?component';
	import PictureAsPdfIcon from '@material-symbols/svg-400/outlined/picture_as_pdf.svg?component';
	import { marked } from 'marked';

	let {
		markdown,
		productName = 'Product',
		onReset
	}: { markdown: string; productName?: string; onReset: () => void } = $props();

	const html = $derived(marked(markdown) as string);

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
      h1 { font-size: 1.8rem; font-weight: 700; margin: 0 0 0.75em; }
      h2 { font-size: 1.35rem; font-weight: 600; margin: 1.75em 0 0.5em; }
      h3 { font-size: 1.1rem; font-weight: 600; margin: 1.25em 0 0.4em; }
      p { margin: 0.6em 0 0.8em; }
      ul, ol { padding-left: 1.5em; margin: 0.5em 0 0.8em; }
      li { margin: 0.3em 0; }
      strong { font-weight: 700; }
      @media print { body { padding: 0; } }
    `;
		win.document.head.appendChild(style);
		win.document.title = `${productName} — Product Report`;
		win.document.body.innerHTML = content;
		win.focus();
		setTimeout(() => win.print(), 250);
	}
</script>

<div class="mx-auto max-w-4xl px-5 py-8 md:px-12 lg:px-20">
	<div class="mb-10 border-b border-pl-rule pb-6">
		<div class="mb-5 flex items-center justify-between">
			<button
				onclick={onReset}
				class="inline-flex cursor-pointer items-center gap-2 rounded-full border border-pl-rule px-3.5 py-2 text-[13px] text-pl-ink transition-colors hover:bg-pl-card"
			>
				← New analysis
			</button>
			<div class="flex gap-2">
				<button
					onclick={copyPlainText}
					title="複製原文"
					aria-label="複製原文"
					class="flex size-8 cursor-pointer items-center justify-center rounded-md border transition-all active:scale-95"
					class:border-green-400={copiedPlain}
					class:border-pl-rule={!copiedPlain}
					class:opacity-50={!copiedPlain}
					class:hover:opacity-100={!copiedPlain}
				>
					<ContentCopyIcon
						class="size-5 {copiedPlain ? 'fill-green-400' : 'fill-pl-ink-2'}"
					/>
				</button>
				<button
					onclick={copyMarkdown}
					title="複製 Markdown"
					aria-label="複製 Markdown"
					class="flex size-8 cursor-pointer items-center justify-center rounded-md border transition-all active:scale-95"
					class:border-green-400={copiedMarkdown}
					class:border-pl-rule={!copiedMarkdown}
					class:opacity-50={!copiedMarkdown}
					class:hover:opacity-100={!copiedMarkdown}
				>
					<MarkdownCopyIcon
						class="size-5 {copiedMarkdown ? 'fill-green-400' : 'fill-pl-ink-2'}"
					/>
				</button>
				<button
					onclick={downloadPdf}
					title="下載 PDF"
					aria-label="下載 PDF"
					class="flex size-8 cursor-pointer items-center justify-center rounded-md border border-pl-rule opacity-50 transition-all hover:opacity-100 active:scale-95"
				>
					<PictureAsPdfIcon class="size-5 fill-pl-ink-2" />
				</button>
			</div>
		</div>
		<h1 class="m-0 font-display text-[clamp(28px,4vw,40px)] font-semibold tracking-[-0.02em]">
			{productName}
		</h1>
	</div>

	<!-- eslint-disable-next-line svelte/no-at-html-tags -->
	<div bind:this={reportEl} class="prose max-w-none prose-stone">{@html html}</div>
</div>
