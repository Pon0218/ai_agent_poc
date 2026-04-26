<script lang="ts">
	import { onMount } from 'svelte';
	import { useGenerateSwot } from '../hooks/useGenerateSwot';
	import LoadingState from './LoadingState.svelte';

	let { sessionId, onComplete }: { sessionId: string; onComplete: (markdown: string) => void } =
		$props();

	const mutation = useGenerateSwot();
	let error = $state<string | null>(null);

	function startPoll() {
		error = null;
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
				onError: (err) => {
					if (!alive) return;
					error = err instanceof Error ? err.message : '分析失敗，請稍後再試';
				}
			});
		};

		poll();
		return () => {
			alive = false;
		};
	}

	onMount(() => {
		const cleanup = startPoll();
		return cleanup;
	});
</script>

{#if error}
	<div class="flex min-h-[70vh] flex-col items-center justify-center gap-6 px-6 py-20">
		<p class="text-center font-ui text-pl-neg">{error}</p>
		<button
			onclick={startPoll}
			class="rounded-pl-sm bg-pl-accent px-6 py-2.5 font-ui text-sm text-pl-bg transition-colors hover:bg-pl-accent-h"
		>
			重新嘗試
		</button>
	</div>
{:else}
	<LoadingState />
{/if}
