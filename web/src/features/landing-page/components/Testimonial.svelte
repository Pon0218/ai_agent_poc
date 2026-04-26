<script lang="ts">
	import coffeeUrl from '../assets/coffee.png?url';
</script>

<section
	id="testimonials"
	class="mx-auto max-w-7xl px-5 py-[clamp(72px,9vw,128px)] md:px-12 lg:px-20"
>
	<div
		class="grid grid-cols-1 overflow-hidden rounded-pl-lg border border-pl-rule md:grid-cols-[5fr_7fr]"
	>
		<div
			class="relative flex min-h-95 flex-col justify-between overflow-hidden p-[clamp(28px,4vw,48px)] text-pl-bg"
			style="background: linear-gradient(180deg, rgba(26,26,24,0.55) 0%, rgba(26,26,24,0.25) 40%, rgba(26,26,24,0.75) 100%), url('{coffeeUrl}') center/cover;"
		>
			<div
				class="pointer-events-none absolute inset-0"
				style="background-image: repeating-linear-gradient(0deg, rgba(245,241,235,0.05) 0 1px, transparent 1px 24px);"
			></div>

			<span
				class="relative z-10 font-mono text-[11px] tracking-[0.14em] uppercase"
				style="color: rgba(245,241,235,0.55);"
			>
				One coffee · one report
			</span>

			<span
				class="relative z-10 mt-auto self-end"
				aria-hidden="true"
				style="filter: blur(4px);"
			>
				<svg
					width="160"
					height="160"
					viewBox="0 0 160 160"
					fill="none"
					xmlns="http://www.w3.org/2000/svg"
				>
					<path
						d="M 150 58 C 160 90, 144 128, 116 144 C 88 160, 48 156, 24 136 C 0 116, -4 80, 8 54 C 20 28, 50 8, 78 8 C 106 8, 132 24, 146 46"
						stroke="rgba(255,255,255,0.82)"
						stroke-width="4.5"
						stroke-linecap="round"
						fill="none"
					/>
				</svg>
			</span>
		</div>

		<div class="flex flex-col justify-center bg-pl-bg p-[clamp(32px,5vw,72px)]">
			<div
				class="mb-6 font-display text-[80px] leading-[0.5] text-pl-ink-3 italic"
				aria-hidden="true"
			>
				"
			</div>
			<blockquote
				class="m-0 mb-8 font-display text-[clamp(22px,2.6vw,32px)] leading-[1.35] font-medium tracking-[-0.01em]"
			>
				One coffee, one report. By the time your espresso cools, you'll have a market
				analysis sharper than anything a consultant ships in a month.
			</blockquote>
		</div>
	</div>
</section>
