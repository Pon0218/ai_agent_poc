<script lang="ts">
	type Mark = 'yes' | 'no' | 'maybe';

	const rows: {
		label: string;
		ours: string;
		diy: { mark: Mark; text: string };
		consultant: { mark: Mark; text: string };
	}[] = [
		{
			label: 'Time to first report',
			ours: 'Under 2 minutes',
			diy: { mark: 'no', text: '2–3 weeks' },
			consultant: { mark: 'no', text: '4–8 weeks' }
		},
		{
			label: 'SWOT with citations',
			ours: 'Built-in',
			diy: { mark: 'maybe', text: 'Manual' },
			consultant: { mark: 'yes', text: 'Included' }
		},
		{
			label: 'Competitor matrix',
			ours: 'Top 5 with pricing',
			diy: { mark: 'maybe', text: 'If you scrape' },
			consultant: { mark: 'yes', text: 'Included' }
		},
		{
			label: 'Refreshes automatically',
			ours: 'Every 24h',
			diy: { mark: 'no', text: 'Stale by week 2' },
			consultant: { mark: 'no', text: 'One-shot deck' }
		},
		{
			label: 'Editable & exportable',
			ours: 'PDF · Notion · CSV',
			diy: { mark: 'yes', text: 'Yes' },
			consultant: { mark: 'maybe', text: 'PDF only' }
		}
	];

	const markClass: Record<Mark, string> = {
		yes: 'bg-[rgba(61,90,58,0.14)] text-pl-pos',
		no: 'bg-[rgba(138,58,46,0.12)] text-pl-neg',
		maybe: 'bg-[rgba(138,110,46,0.12)] text-pl-warn'
	};

	const markIcon: Record<Mark, string> = { yes: '✓', no: '✗', maybe: '~' };
</script>

<section id="pricing" class="mx-auto max-w-7xl px-5 py-[clamp(72px,9vw,128px)] md:px-12 lg:px-20">
	<header class="mb-14 text-center">
		<span class="font-mono text-[12px] tracking-[0.14em] text-pl-ink-2 uppercase">
			The case for ProductLens
		</span>
		<h2
			class="mt-3 mb-0 font-display text-[clamp(36px,5vw,64px)] font-semibold tracking-[-0.02em]"
		>
			Why <em class="font-normal text-pl-ink-2 italic">ProductLens?</em>
		</h2>
		<p class="m-0 mx-auto mt-3 max-w-[56ch] text-pl-ink-2">
			Same depth as a consultant, same speed as a search bar.
		</p>
	</header>

	<div class="overflow-hidden rounded-pl-md border border-pl-rule bg-pl-bg">
		<!-- header row -->
		<div
			class="hidden border-b border-pl-rule md:grid"
			style="grid-template-columns: 1.6fr 1fr 1fr 1fr;"
		>
			<div
				class="px-6 py-5.5 font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
			></div>
			<div
				class="border-b border-pl-rule bg-pl-ink px-6 py-5.5 font-mono text-[11px] tracking-[0.14em] text-pl-bg uppercase"
			>
				ProductLens
			</div>
			<div
				class="px-6 py-5.5 font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
			>
				DIY research
			</div>
			<div
				class="px-6 py-5.5 font-mono text-[11px] tracking-[0.14em] text-pl-ink-2 uppercase"
			>
				Hire a consultant
			</div>
		</div>

		{#each rows as row (row.label)}
			<div
				class="grid grid-cols-1 border-b border-pl-rule last:border-b-0 md:grid-cols-[1.6fr_1fr_1fr_1fr]"
			>
				<div class="px-6 py-5.5 font-display text-[16px] font-medium text-pl-ink">
					{row.label}
				</div>
				<div
					class="flex items-center gap-2.5 bg-pl-card px-6 py-5.5 text-[14px] text-pl-ink"
				>
					<span
						class="inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-full text-[12px] {markClass.yes}"
					>
						✓
					</span>
					{row.ours}
				</div>
				{#each [row.diy, row.consultant] as cell (cell.text)}
					<div class="flex items-center gap-2.5 px-6 py-5.5 text-[14px] text-pl-ink-2">
						<span
							class="inline-flex h-5 w-5 shrink-0 items-center justify-center rounded-full text-[12px] {markClass[
								cell.mark
							]}"
						>
							{markIcon[cell.mark]}
						</span>
						{cell.text}
					</div>
				{/each}
			</div>
		{/each}
	</div>
</section>
