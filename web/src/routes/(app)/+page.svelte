<script lang="ts">
	import ProductLensForm from '@/features/ProductLens/components/ProductLensForm.svelte';
	import ProductLensLoading from '@/features/ProductLens/components/ProductLensLoading.svelte';
	import ProductLensReport from '@/features/ProductLens/components/ProductLensReport.svelte';

	type Stage = 'form' | 'loading' | 'report';

	let stage = $state<Stage>('form');
	let sessionId = $state('');
	let reportMarkdown = $state('');

	function handleFormSuccess(id: string) {
		sessionId = id;
		stage = 'loading';
	}

	function handleReportReady(markdown: string) {
		reportMarkdown = markdown;
		stage = 'report';
	}
</script>

{#if stage === 'form'}
	<ProductLensForm onSuccess={handleFormSuccess} />
{:else if stage === 'loading'}
	<ProductLensLoading {sessionId} onComplete={handleReportReady} />
{:else}
	<ProductLensReport markdown={reportMarkdown} />
{/if}
