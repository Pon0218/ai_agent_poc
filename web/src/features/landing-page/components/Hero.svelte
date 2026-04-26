<script lang="ts">
	import { goto } from '$app/navigation';
	import { QuickInput } from '@/components/ui/quick-input';

	function handleQuickSubmit(url: string) {
		if (url) sessionStorage.setItem('pl:url', url);
		goto('/analyze');
	}
</script>

<section
	class="mx-auto max-w-7xl px-5 pt-[clamp(80px,11vw,160px)] pb-[clamp(60px,8vw,110px)] md:px-12 lg:px-20"
>
	<div class="grid grid-cols-1 items-end gap-6 xl:grid-cols-[1.1fr_0.9fr] xl:gap-20">
		<div>
			<div class="mb-7 flex items-center gap-2.5">
				<span class="h-1.5 w-1.5 rounded-full bg-pl-ink"></span>
				<span class="font-mono text-[12px] tracking-[0.14em] text-pl-ink-2 uppercase">
					AI Industry Reports · v2.0
				</span>
			</div>

			<h1
				class="mb-6 max-w-[14ch] font-display text-[clamp(44px,7vw,92px)] leading-[1.04] font-semibold tracking-[-0.02em] text-pl-ink"
			>
				Drop a&nbsp;URL.<br />Get a full product report.
			</h1>

			<p
				class="mb-12 max-w-[36ch] font-display text-[clamp(20px,2.2vw,28px)] font-normal text-pl-ink-2 italic"
			>
				Hi, what are you building?
			</p>

			<QuickInput onsubmit={handleQuickSubmit} />

			<div class="mt-4.5 flex flex-wrap gap-4.5 text-[13px] text-pl-ink-2">
				<span class="before:mr-2 before:text-pl-ink before:opacity-55 before:content-['✓']"
					>No credit card</span
				>
				<span class="before:mr-2 before:text-pl-ink before:opacity-55 before:content-['✓']"
					>2-minute analysis</span
				>
				<span class="before:mr-2 before:text-pl-ink before:opacity-55 before:content-['✓']"
					>Export to PDF</span
				>
			</div>
		</div>

		<aside
			class="relative hidden aspect-4/5 flex-col justify-between overflow-hidden rounded-pl-lg border border-pl-rule p-5.5 xl:flex"
			style="background: repeating-linear-gradient(135deg, rgba(26,26,24,0.04) 0 1px, transparent 1px 12px), linear-gradient(180deg, #E8E3DA 0%, #DED7CB 100%);"
			aria-hidden="true"
		>
			<span
				class="self-start rounded-md px-2.5 py-1.5 font-mono text-[11px] tracking-widest text-pl-ink uppercase"
				style="background: rgba(26,26,24,0.06);"
			>
				SCAN · 0421
			</span>

			<span
				class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 rounded-full"
				style="width: 62%; aspect-ratio: 1; background: radial-gradient(circle at 35% 35%, rgba(255,255,255,0.55) 0 8%, transparent 12%), radial-gradient(circle at 50% 50%, #1A1A18 0 70%, transparent 71%); box-shadow: 0 30px 60px -30px rgba(0,0,0,0.4), inset 0 0 0 6px #EFEAE0;"
			>
				<span
					class="absolute rounded-full border border-dashed"
					style="inset: 18%; border-color: rgba(245,241,235,0.35);"
				></span>
			</span>

			<div
				class="relative z-10 flex justify-between font-mono text-[11px] tracking-[0.06em] text-pl-ink-2"
			>
				<span>LAT 37.77</span>
				<span>LON -122.42</span>
			</div>
		</aside>
	</div>
</section>
