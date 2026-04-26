<script lang="ts">
	import ProductLensForm from '@/features/ProductLens/components/ProductLensForm.svelte';
	import ProductLensLoading from '@/features/ProductLens/components/ProductLensLoading.svelte';
	import ProductLensReport from '@/features/ProductLens/components/ProductLensReport.svelte';

	let stage = $state<'form' | 'loading' | 'report'>('form');
	let sessionId = $state('');
	let productName = $state('');
	let reportMarkdown = $state('');

	function handleFormSuccess(id: string, name: string) {
		sessionId = id;
		productName = name;
		stage = 'loading';
	}

	function handleReportReady(markdown: string) {
		reportMarkdown = markdown;
		stage = 'report';
	}

	function handleReset() {
		stage = 'form';
		sessionId = '';
		productName = '';
		reportMarkdown = '';
	}
</script>

{#if stage === 'form'}
	<ProductLensForm onSuccess={handleFormSuccess} />
{:else if stage === 'loading'}
	<ProductLensLoading {sessionId} onComplete={handleReportReady} />
{:else}
	<ProductLensReport markdown={reportMarkdown} {productName} onReset={handleReset} />
{/if}
