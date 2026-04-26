<script lang="ts">
</script>

<section id="features" class="mx-auto max-w-7xl px-5 py-[clamp(72px,9vw,128px)] md:px-12 lg:px-20">
	<header class="mb-16 grid grid-cols-1 items-end gap-10 md:grid-cols-2">
		<h2
			class="m-0 font-display text-[clamp(36px,5vw,64px)] leading-[1.05] font-semibold tracking-[-0.02em] text-pl-ink"
		>
			We've cracked <em class="font-normal text-pl-ink-2 italic">the code.</em>
		</h2>
		<p class="m-0 max-w-[44ch] text-[16px] text-pl-ink-2">
			Four lenses on every product you analyze — wired together so insight stays in context,
			not in tabs.
		</p>
	</header>

	<div
		class="grid grid-cols-2 gap-px overflow-hidden rounded-pl-md border border-pl-rule bg-pl-rule lg:grid-cols-4"
	>
		{#each [{ num: '01', title: 'Market Analysis', desc: '產業現況、規模估算與三年成長曲線，直接落地到你的產品定位。', icon: `<path d="M3 18 L8 12 L12 14 L19 5" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/><circle cx="19" cy="5" r="1.4" fill="currentColor"/>` }, { num: '02', title: 'SWOT Report', desc: '優劣、機會、威脅四象限，每一條都附上推論依據與引用。', icon: `<rect x="3" y="3" width="7" height="7" stroke="currentColor" stroke-width="1.6"/><rect x="12" y="3" width="7" height="7" stroke="currentColor" stroke-width="1.6"/><rect x="3" y="12" width="7" height="7" stroke="currentColor" stroke-width="1.6"/><rect x="12" y="12" width="7" height="7" stroke="currentColor" stroke-width="1.6"/>` }, { num: '03', title: 'Competitor Intel', desc: '找出 Top 5 競品、定價、市佔與差異化角度。', icon: `<circle cx="11" cy="11" r="8" stroke="currentColor" stroke-width="1.6"/><circle cx="11" cy="11" r="3.5" stroke="currentColor" stroke-width="1.6"/><path d="M11 1.5 V20.5 M1.5 11 H20.5" stroke="currentColor" stroke-width="1.2" opacity="0.4"/>` }, { num: '04', title: 'Actionable Insights', desc: '不是 dashboard，是行動清單 — 下週、下月、下季可執行的策略。', icon: `<path d="M11 2 L13.5 8 L20 8.5 L15 13 L16.5 19.5 L11 16 L5.5 19.5 L7 13 L2 8.5 L8.5 8 Z" stroke="currentColor" stroke-width="1.4" stroke-linejoin="round"/>` }] as feat (feat.num)}
			<article class="flex min-h-70 flex-col gap-4 bg-pl-bg p-[28px_28px_36px]">
				<div
					class="flex h-11 w-11 items-center justify-center rounded-[10px] bg-pl-card text-pl-ink"
					aria-hidden="true"
				>
					<svg width="22" height="22" viewBox="0 0 22 22" fill="none">
						<!-- eslint-disable-next-line svelte/no-at-html-tags -->
						{@html feat.icon}
					</svg>
				</div>
				<h3
					class="m-0 font-display text-[20px] font-semibold tracking-[-0.01em] text-pl-ink"
				>
					{feat.title}
				</h3>
				<p class="m-0 text-[14px] leading-[1.6] text-pl-ink-2">{feat.desc}</p>
				<span class="mt-auto font-mono text-[11px] tracking-[0.12em] text-pl-ink-3">
					— {feat.num}
				</span>
			</article>
		{/each}
	</div>
</section>
