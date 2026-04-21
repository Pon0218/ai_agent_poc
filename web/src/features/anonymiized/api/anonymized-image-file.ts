import { z } from 'zod';
import { env } from '@/config/env';
import { anonymized_api } from '@/lib/api-client';

// ---------------------------------- API URL ----------------------------------------------------
export const url = `${env.API_URL}/anonymized-image-file`;

// --------------------------------- typeScript 型別定義 ----------------------------------------------

export const InputSchema = z.object({
	image: z.instanceof(File),
	input_text: z.string(),
	language: z.enum(['zh', 'en']),
	model: z.literal('gpt-4.1')
});

export const OutputSchema = z.object({
	result: z.string(),
	llm_output: z.string(),
	mapping_table: z.record(z.string()),
	deanonymization_applied: z.boolean(),
	deanonymization_ok: z.boolean(),
	deanonymization_false_reasons: z.array(
		z.enum(['no_mapping_generated', 'unresolved_tokens_after_deanonymization'])
	)
});

export type InputType = z.infer<typeof InputSchema>;
export type OutputType = z.infer<typeof OutputSchema>;

// ---------------------------------- 2. Fetcher Function ----------------------------------------------------

export async function callAnonymizedImageFile(payload: InputType): Promise<OutputType> {
	const res = await anonymized_api.postForm(url, payload);
	return OutputSchema.parse(res);
}

// ---------------------------------- 3. Mutation Options ----------------------------------------------------
// Not required for mutations in most cases.
