<script lang="ts">
	import { useCreateSession } from '../hooks/useCreateSession';
	import type { InputType } from '../api/sessions';

	let { onSuccess }: { onSuccess: (sessionId: string) => void } = $props();

	let productName = $state('');
	let websiteUrl = $state('');
	let productDescription = $state('');
	let submitted = $state(false);

	const mutation = useCreateSession();

	const nameValid = $derived(productName.trim().length > 0);
	const urlValid = $derived(websiteUrl.trim().length > 0);
	const descValid = $derived(productDescription.trim().length > 0);
	const canSubmit = $derived(nameValid && urlValid && descValid && !mutation.isPending);

	$effect(() => {
		if (mutation.isSuccess && mutation.data) {
			onSuccess(mutation.data.data.session_id);
		}
	});

	function handleSubmit() {
		submitted = true;
		if (!canSubmit) return;
		const payload: InputType = {
			product_name: productName,
			website_url: websiteUrl,
			product_description: productDescription
		};
		mutation.mutate(payload);
	}
</script>

<div class="flex w-full flex-col items-center gap-6 px-4 py-8">
	<div class="flex flex-col items-center gap-2 text-center">
		<p
			class="font-['Playfair_Display'] text-2xl leading-tight text-s-sub-headline italic md:text-3xl"
		>
			Hi, what are you building?
		</p>
		<p class="font-['Playfair_Display'] text-2xl leading-tight text-s-headline md:text-3xl">
			Drop a URL. Get a full product report.
		</p>
	</div>

	<div class="w-full max-w-xl">
		<div
			class="overflow-hidden rounded-2xl bg-s-card-background/60 shadow-[0_4px_24px_rgba(0,0,0,0.06)] backdrop-blur-[42px]"
		>
			<!-- 產品名稱 -->
			<label
				class="block px-5 pt-4 pb-3"
				class:border-b={true}
				style="border-bottom: 1px solid rgba(0,0,0,0.06)"
			>
				<span
					class="mb-1 block text-[11px] font-semibold tracking-wider text-s-sub-headline uppercase"
				>
					產品名稱
					{#if submitted && !nameValid}<span class="ml-1 text-red-400">必填</span>{/if}
				</span>
				<input
					bind:value={productName}
					placeholder="e.g. Notion、Figma、你的 SaaS"
					autocomplete="off"
					class="w-full bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
				/>
			</label>

			<!-- 產品網址 -->
			<label class="block px-5 pt-4 pb-3" style="border-bottom: 1px solid rgba(0,0,0,0.06)">
				<span
					class="mb-1 block text-[11px] font-semibold tracking-wider text-s-sub-headline uppercase"
				>
					產品網址
					{#if submitted && !urlValid}<span class="ml-1 text-red-400">必填</span>{/if}
				</span>
				<input
					bind:value={websiteUrl}
					placeholder="https://example.com"
					type="url"
					autocomplete="url"
					class="w-full bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
				/>
			</label>

			<!-- 產品敘述 -->
			<label class="block px-5 pt-4 pb-3">
				<span
					class="mb-1 block text-[11px] font-semibold tracking-wider text-s-sub-headline uppercase"
				>
					產品敘述
					{#if submitted && !descValid}<span class="ml-1 text-red-400">必填</span>{/if}
				</span>
				<textarea
					bind:value={productDescription}
					placeholder="這個產品解決什麼問題？目標用戶是誰？"
					rows="3"
					class="w-full resize-none bg-transparent text-sm text-s-headline placeholder:text-s-placeholder focus:outline-none"
				></textarea>
			</label>
		</div>

		{#if mutation.isError}
			<p role="alert" class="mt-2 px-1 text-xs text-red-400">
				Something went wrong. Please try again.
			</p>
		{/if}

		<div class="mt-3 flex justify-end">
			<button
				onclick={handleSubmit}
				disabled={mutation.isPending}
				aria-busy={mutation.isPending}
				class="cursor-pointer rounded-xl bg-s-button px-6 py-2.5 font-['Playfair_Display'] text-sm text-s-main shadow-sm transition-all hover:opacity-85 active:scale-95 disabled:cursor-not-allowed disabled:opacity-40"
			>
				{mutation.isPending ? 'Analyzing...' : 'Analyze →'}
			</button>
		</div>
	</div>
</div>
