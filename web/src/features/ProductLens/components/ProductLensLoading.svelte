<script lang="ts">
	import { onMount } from 'svelte';
	import { useGenerateSwot } from '../hooks/useGenerateSwot';
	import LoadingState from './LoadingState.svelte';

	let { sessionId, onComplete }: { sessionId: string; onComplete: (markdown: string) => void } =
		$props();

	const mutation = useGenerateSwot();

	onMount(() => {
		let alive = true;

		const poll = () => {
			if (!alive) return;
			mutation.mutate(sessionId, {
				onSuccess: (result) => {
					if (!alive) return;
					if (result.data.swot_markdown) {
						onComplete(result.data.swot_markdown);
					} else {
						setTimeout(poll, 3000);
					}
				},
				onError: () => {
					if (alive) setTimeout(poll, 3000);
				}
			});
		};

		poll();
		return () => {
			alive = false;
		};
	});
</script>

<LoadingState />
