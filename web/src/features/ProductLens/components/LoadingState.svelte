<script lang="ts">
	const messages = [
		'Researching the market…',
		'Identifying competitors…',
		'Generating your report…'
	];

	let activeIndex = $state(0);
	let visible = $state(true);

	$effect(() => {
		const prefersReduced =
			typeof window !== 'undefined' &&
			window.matchMedia('(prefers-reduced-motion: reduce)').matches;
		if (prefersReduced) return;

		const cycle = () => {
			visible = false;
			setTimeout(() => {
				activeIndex = (activeIndex + 1) % messages.length;
				visible = true;
			}, 250);
		};

		const t1 = setTimeout(cycle, 1500);
		const t2 = setTimeout(cycle, 3000);
		return () => {
			clearTimeout(t1);
			clearTimeout(t2);
		};
	});
</script>

<div class="flex min-h-[70vh] flex-col items-center justify-center gap-8 px-6 py-20">
	<div class="flex gap-2.5" aria-hidden="true">
		{#each [0, 1, 2] as i (i)}
			<span
				class="h-2.5 w-2.5 rounded-full bg-pl-ink"
				style="animation: pl-pulse 1.2s infinite ease-in-out; animation-delay: {i * 0.18}s;"
			></span>
		{/each}
	</div>

	<p
		class="font-display text-[clamp(20px,2.5vw,28px)] text-pl-ink-2 italic transition-opacity duration-400"
		style="opacity: {visible ? 1 : 0};"
	>
		{messages[activeIndex]}
	</p>
</div>

<style>
	@keyframes pl-pulse {
		0%,
		60%,
		100% {
			opacity: 0.18;
			transform: translateY(0);
		}
		30% {
			opacity: 1;
			transform: translateY(-6px);
		}
	}
</style>
