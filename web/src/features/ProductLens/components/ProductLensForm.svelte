<script lang="ts">
	import { useCreateSession } from '../hooks/useCreateSession';
	import type { InputType } from '../api/sessions';

	let { onSuccess }: { onSuccess: (sessionId: string) => void } = $props();

	let productName = $state('');
	let websiteUrl = $state('');
	let productDescription = $state('');

	const mutation = useCreateSession();

	const canSubmit = $derived(productName.trim().length > 0 && !mutation.isPending);

	$effect(() => {
		if (mutation.isSuccess && mutation.data) {
			onSuccess(mutation.data.data.session_id);
		}
	});

	function handleSubmit() {
		if (!canSubmit) return;
		const payload: InputType = {
			product_name: productName,
			website_url: websiteUrl || null,
			product_description: productDescription || null
		};
		mutation.mutate(payload);
	}
</script>

<div class="flex w-full flex-col items-center gap-6 px-4 py-10">
	<div class="flex flex-col items-center gap-3 text-center">
		<p
			class="font-['Playfair_Display'] text-3xl leading-tight text-s-sub-headline italic md:text-[36px]"
		>
			Hi, what are you building?
		</p>
		<p class="font-['Playfair_Display'] text-3xl leading-tight text-s-headline md:text-[36px]">
			Drop a URL. Get a full product report.
		</p>
	</div>

	<div class="flex w-full max-w-152 flex-col gap-3">
		<div
			class="rounded-2xl bg-s-card-background/50 px-5 py-4 shadow-[0_4px_24px_rgba(0,0,0,0.04)] backdrop-blur-[42px]"
		>
			<input
				bind:value={productName}
				placeholder="產品名稱"
				class="w-full bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
			/>
		</div>

		<div
			class="rounded-2xl bg-s-card-background/50 px-5 py-4 shadow-[0_4px_24px_rgba(0,0,0,0.04)] backdrop-blur-[42px]"
		>
			<input
				bind:value={websiteUrl}
				placeholder="產品網址"
				type="url"
				class="w-full bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
			/>
		</div>

		<div
			class="rounded-2xl bg-s-card-background/50 px-5 py-4 shadow-[0_4px_24px_rgba(0,0,0,0.04)] backdrop-blur-[42px]"
		>
			<textarea
				bind:value={productDescription}
				placeholder="產品敘述"
				rows="3"
				class="w-full resize-none bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
			></textarea>
		</div>

		<div class="flex items-center justify-end gap-3">
			{#if mutation.isError}
				<p class="text-xs text-red-400">Something went wrong. Please try again.</p>
			{/if}
			<button
				onclick={handleSubmit}
				disabled={!canSubmit}
				class="cursor-pointer rounded-md bg-s-button px-3 py-1 font-['Playfair_Display'] text-sm text-s-main transition-opacity hover:opacity-80 disabled:cursor-not-allowed disabled:opacity-50"
			>
				{mutation.isPending ? 'Analyzing...' : 'Analyze'}
			</button>
		</div>
	</div>
</div>
