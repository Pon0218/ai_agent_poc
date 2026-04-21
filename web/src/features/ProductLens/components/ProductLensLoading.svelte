<script lang="ts">
	import { fade } from 'svelte/transition';
	import { generateSwot } from '../api/swot-generate';

	let { sessionId, onComplete }: { sessionId: string; onComplete: (markdown: string) => void } =
		$props();

	const messages = [
		'Understanding the core features...',
		'Structuring the report...',
		'Almost there...'
	];

	let activeIndex = $state(0);
	let visible = $state(true);

	const prefersReducedMotion =
		typeof window !== 'undefined' &&
		window.matchMedia('(prefers-reduced-motion: reduce)').matches;

	$effect(() => {
		if (prefersReducedMotion) return;

		const cycle = () => {
			visible = false;
			setTimeout(() => {
				activeIndex = (activeIndex + 1) % messages.length;
				visible = true;
			}, 400);
		};

		const timer = setInterval(cycle, 2800);
		return () => clearInterval(timer);
	});

	$effect(() => {
		let alive = true;

		(async () => {
			while (alive) {
				try {
					const result = await generateSwot(sessionId);
					if (result.data.swot_markdown) {
						if (alive) onComplete(result.data.swot_markdown);
						return;
					}
				} catch {
					// silently retry
				}
				await new Promise((r) => setTimeout(r, 3000));
			}
		})();

		return () => {
			alive = false;
		};
	});
</script>

<div class="flex w-full flex-col items-center justify-center px-4 py-24">
	<div class="flex h-14 flex-col items-center justify-center text-center">
		{#if visible}
			<p
				in:fade={{ duration: 400 }}
				out:fade={{ duration: 300 }}
				class="font-['Playfair_Display'] text-2xl leading-snug text-s-sub-headline italic md:text-3xl"
			>
				{messages[activeIndex]}
			</p>
		{/if}
	</div>
</div>
