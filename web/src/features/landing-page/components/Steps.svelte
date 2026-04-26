<script lang="ts">
</script>

<section id="how" class="mx-auto max-w-7xl px-5 py-[clamp(72px,9vw,128px)] md:px-12 lg:px-20">
	<header class="mb-18 grid grid-cols-1 items-end gap-10 md:grid-cols-2">
		<h2 class="m-0 font-display text-[clamp(36px,5vw,64px)] font-semibold tracking-[-0.02em]">
			Three steps to <em class="font-normal text-pl-ink-2 italic">clarity.</em>
		</h2>
		<p class="m-0 max-w-[44ch] text-pl-ink-2">
			You bring a URL. We bring the report. Everything else is editing, exporting and sharing.
		</p>
	</header>

	<div class="grid grid-cols-1 border-t border-pl-rule md:grid-cols-3">
		{#each [{ n: '01', title: '輸入產品資訊', desc: "Paste a URL, a product name, or a one-line description. Anything we can crawl, we'll work with.", tag: '~ 30 seconds' }, { n: '02', title: 'AI 分析產業', desc: 'We pull market signals, identify competitors and triangulate positioning across 14 dimensions.', tag: '~ 90 seconds' }, { n: '03', title: '獲得完整報告', desc: 'A single document — SWOT, market sizing, competitor matrix, recommendations — with citations.', tag: 'ready to share' }] as step, i (step.n)}
			<article
				class="relative flex min-h-70 flex-col gap-4 p-[40px_32px_32px]"
				class:border-r={i < 2}
				class:border-pl-rule={i < 2}
				class:md:border-r-pl-rule={true}
			>
				<span
					class="font-display text-[clamp(64px,9vw,112px)] leading-[0.9] font-semibold tracking-[-0.04em] text-pl-ink"
				>
					{step.n}
				</span>
				<h4 class="m-0 font-display text-[22px] font-semibold tracking-[-0.01em]">
					{step.title}
				</h4>
				<p class="m-0 max-w-[32ch] text-[14px] text-pl-ink-2">{step.desc}</p>
				<span
					class="mt-auto font-mono text-[11px] tracking-[0.12em] text-pl-ink-3 uppercase"
				>
					{step.tag}
				</span>
			</article>
		{/each}
	</div>
</section>
