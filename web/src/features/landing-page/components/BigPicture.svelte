<script lang="ts">
</script>

<section id="big" class="mx-auto max-w-7xl px-5 py-[clamp(72px,9vw,128px)] md:px-12 lg:px-20">
	<div class="grid grid-cols-1 items-center gap-[clamp(32px,6vw,96px)] md:grid-cols-2">
		<div>
			<span class="font-mono text-[12px] tracking-[0.14em] text-pl-ink-2 uppercase">
				The full report
			</span>
			<h2
				class="mt-4 mb-6 font-display text-[clamp(36px,4.5vw,56px)] leading-[1.05] font-semibold tracking-[-0.02em]"
			>
				See the <em class="font-normal text-pl-ink-2 italic">big picture</em>, not the
				noise.
			</h2>
			<p class="mb-8 max-w-[44ch] text-[17px] text-pl-ink-2">
				Every report is a single, navigable document — no slides, no spreadsheets, no
				copy-paste between tabs.
			</p>
			<ul class="m-0 list-none p-0">
				{#each [{ n: '01', title: 'Market sizing & growth', desc: 'TAM / SAM / SOM 估算、三年趨勢線、地理分佈。' }, { n: '02', title: 'SWOT with citations', desc: '每一個結論都帶來源連結，可以追溯也可以反駁。' }, { n: '03', title: 'Competitor matrix & moves', desc: 'Top 5 競品、定價方案、近 90 天的產品動態。' }] as item (item.n)}
					<li
						class="grid gap-4 border-t border-pl-rule py-5 last:border-b last:border-pl-rule"
						style="grid-template-columns: 28px 1fr;"
					>
						<span class="mt-1 font-mono text-[12px] tracking-widest text-pl-ink-2"
							>{item.n}</span
						>
						<div>
							<h4 class="m-0 mb-1 font-display text-[18px] font-semibold">
								{item.title}
							</h4>
							<p class="m-0 text-[14px] text-pl-ink-2">{item.desc}</p>
						</div>
					</li>
				{/each}
			</ul>
		</div>

		<aside
			class="relative flex aspect-4/5 items-center justify-center overflow-hidden rounded-pl-lg border border-pl-rule p-7"
			style="background: repeating-linear-gradient(45deg, rgba(26,26,24,0.05) 0 1px, transparent 1px 14px), linear-gradient(160deg, #E8E3DA 0%, #DED7CB 100%);"
			aria-hidden="true"
		>
			<div
				class="flex w-[88%] flex-col gap-3.5 rounded-xl border border-pl-rule bg-pl-bg p-5.5"
				style="box-shadow: 0 30px 60px -30px rgba(0,0,0,0.25), 0 1px 0 rgba(0,0,0,0.04);"
			>
				<div class="flex items-center justify-between">
					<span class="font-display text-[16px] font-semibold">Market Health</span>
					<span
						class="rounded-sm bg-pl-card px-2 py-1 font-mono text-[10px] tracking-widest text-pl-ink-2 uppercase"
						>Q2 · 2026</span
					>
				</div>
				{#each [{ label: 'TAM growth', val: '+18.4%', width: '70%' }, { label: 'Competitor density', val: 'Med', width: '44%' }, { label: 'Pricing pressure', val: 'Low', width: '84%' }, { label: 'Time-to-market', val: '4–6 wks', width: '30%' }] as row (row.label)}
					<div class="relative h-1.5 rounded-[3px] bg-pl-card">
						<span
							class="absolute inset-y-0 left-0 rounded-[3px] bg-pl-ink"
							style="width: {row.width};"
						></span>
					</div>
					<div class="flex justify-between font-mono text-[12px] text-pl-ink-2">
						<span>{row.label}</span>
						<span>{row.val}</span>
					</div>
				{/each}
			</div>
		</aside>
	</div>
</section>
