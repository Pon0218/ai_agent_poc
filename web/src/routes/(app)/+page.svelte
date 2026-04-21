<script lang="ts">
	import { getContext } from 'svelte';
	import ProductLensForm from '@/features/ProductLens/components/ProductLensForm.svelte';
	import ProductLensLoading from '@/features/ProductLens/components/ProductLensLoading.svelte';
	import ProductLensReport from '@/features/ProductLens/components/ProductLensReport.svelte';

	type Stage = 'form' | 'loading' | 'report';
	type AppContext = {
		stage: Stage;
		sessionId: string;
		reportMarkdown: string;
		reset: () => void;
	};

	const ctx = getContext<AppContext>('app');

	function handleFormSuccess(id: string) {
		ctx.sessionId = id;
		ctx.stage = 'loading';
	}

	function handleReportReady(markdown: string) {
		ctx.reportMarkdown = markdown;
		ctx.stage = 'report';
	}
</script>

{#if ctx.stage === 'form'}
	<ProductLensForm onSuccess={handleFormSuccess} />
{:else if ctx.stage === 'loading'}
	<ProductLensLoading sessionId={ctx.sessionId} onComplete={handleReportReady} />
{:else}
	<ProductLensReport markdown={ctx.reportMarkdown} onReset={ctx.reset} />
{/if}
