import { z } from 'zod';
import { env } from '@/config/env';
import { anonymized_api } from '@/lib/api-client';

// ---------------------------------- API URL ----------------------------------------------------
export const url = `${env.API_URL}/anonymized-chat`;

// --------------------------------- 1. Zod Schema & TypeScript Types ----------------------------------------------

export const InputSchema = z.object({
	text: z.string().min(1),
	language: z.enum(['zh', 'en']),
	model: z.string()
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

export async function callAnonymizedChat(payload: InputType): Promise<OutputType> {
	const res = await anonymized_api.post(url, payload);
	return OutputSchema.parse(res);
}

// ---------------------------------- 3. Mutation Options ----------------------------------------------------
// Not required for mutations in most cases.
