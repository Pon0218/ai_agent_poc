<script lang="ts">
	import { marked } from 'marked';
	import ContentCopyIcon from '@material-symbols/svg-400/outlined/content_copy.svg?component';
	import MarkdownCopyIcon from '@material-symbols/svg-400/outlined/markdown_copy.svg?component';
	import PictureAsPdfIcon from '@material-symbols/svg-400/outlined/picture_as_pdf.svg?component';

	let { markdown }: { markdown: string } = $props();

	const renderedHtml = $derived(marked.parse(markdown) as string);

	let reportEl = $state<HTMLElement | null>(null);

	function copyPlainText() {
		const text = reportEl?.innerText ?? markdown;
		navigator.clipboard.writeText(text);
	}

	function copyMarkdown() {
		navigator.clipboard.writeText(markdown);
	}

	function downloadPdf() {
		window.print();
	}
</script>

<svelte:head>
	<style>
		@media print {
			body * {
				visibility: hidden !important;
			}
			.print-report,
			.print-report * {
				visibility: visible !important;
			}
			.print-report {
				position: fixed;
				inset: 0;
				padding: 2rem;
				background: white;
			}
		}
	</style>
</svelte:head>

<div class="w-full px-4 py-6 md:px-8">
	<!-- Toolbar -->
	<div class="mb-4 flex justify-end gap-3">
		<button
			onclick={copyPlainText}
			title="複製原文"
			class="flex size-8 cursor-pointer items-center justify-center rounded-md border border-s-button opacity-50 transition-opacity hover:opacity-100"
		>
			<ContentCopyIcon class="size-5 fill-s-button" />
		</button>
		<button
			onclick={copyMarkdown}
			title="複製 Markdown"
			class="flex size-8 cursor-pointer items-center justify-center rounded-md border border-s-button opacity-50 transition-opacity hover:opacity-100"
		>
			<MarkdownCopyIcon class="size-5 fill-s-button" />
		</button>
		<button
			onclick={downloadPdf}
			title="下載 PDF"
			class="flex size-8 cursor-pointer items-center justify-center rounded-md border border-s-button opacity-50 transition-opacity hover:opacity-100"
		>
			<PictureAsPdfIcon class="size-5 fill-s-button" />
		</button>
	</div>

	<!-- Report Content -->
	<div
		bind:this={reportEl}
		class="print-report mx-auto prose prose-sm max-w-[720px] md:prose-base"
	>
		<!-- eslint-disable-next-line svelte/no-at-html-tags -->
		{@html renderedHtml}
	</div>
</div>
