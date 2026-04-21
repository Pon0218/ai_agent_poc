<script lang="ts">
	import { generateSwot } from '../api/swot-generate';

	let { sessionId, onComplete }: { sessionId: string; onComplete: (markdown: string) => void } =
		$props();

	const messages = [
		'Understanding the core features...',
		'Structuring the report...',
		'Almost there...'
	];

	let activeIndex = $state(0);

	$effect(() => {
		const timer = setInterval(() => {
			activeIndex = (activeIndex + 1) % messages.length;
		}, 2500);
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

<div class="flex w-full flex-col items-center justify-center px-4 py-20">
	<div class="flex flex-col items-center gap-1 text-center">
		{#each messages as msg, i (msg)}
			<p
				class="font-['Playfair_Display'] text-2xl leading-snug text-s-sub-headline italic transition-opacity duration-700 md:text-[36px] md:leading-[36px]"
				class:opacity-100={activeIndex === i}
				class:opacity-20={activeIndex !== i}
			>
				{msg}
			</p>
		{/each}
	</div>
</div>
